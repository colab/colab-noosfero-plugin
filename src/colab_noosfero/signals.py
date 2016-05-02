import logging

import requests

from django.db.models.signals import pre_save
from django.conf import settings
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from colab.signals.signals import send
from .models import NoosferoUser, NoosferoSoftwareCommunity
from colab.accounts.signals import (user_basic_info_updated, delete_user)

LOGGER = logging.getLogger('colab.plugins.noosfero')

@receiver(pre_save, sender=NoosferoSoftwareCommunity)
def verify_community_creation(sender, **kwargs):
    software_community = kwargs.get('instance')
    try:
        NoosferoSoftwareCommunity.objects.get(pk=software_community.id)
    except ObjectDoesNotExist:
        send('community_creation', 'noosfero',
             community=software_community.community)
    else:
        send('community_updated', 'noosfero',
             community=software_community.community)


@receiver(user_basic_info_updated)
def update_basic_info_noosfero_user(sender, **kwargs):
    user = kwargs.get('user')
    update_email = kwargs.get('update_email')
    noosfero_user = NoosferoUser.objects.filter(username=user.username).first()

    if not noosfero_user:
        return

    app_config = settings.COLAB_APPS.get('colab_noosfero', {})
    upstream = app_config.get('upstream', '').rstrip('/')
    verify_ssl = app_config.get('verify_ssl', True)

    users_endpoint = '{}/api/v1/people/{}'.format(upstream, noosfero_user.id)

    params = {
        'id': noosfero_user.id,
        'person[name]': user.get_full_name(),
        'person[personal_website]': user.webpage
    }

    if update_email:
        params['person[email]'] = user.email

    error_msg = u'Error trying to update "%s"\'s basic info on Noosfero. Reason: %s'
    try:
        headers = {'Remote-User': user.username}
        response = requests.post(users_endpoint, params=params,
                                 verify=verify_ssl,headers=headers)
    except Exception as excpt:
        reason = 'Request to API failed ({})'.format(excpt)
        LOGGER.error(error_msg, user.username, reason)
        return

    if response.status_code != 201:
        reason = 'Unknown.'

        try:
            fail_data = response.json()

        except ValueError as value_error:
            reason = '{} :: {}'.format(response.status_code,
                                       value_error.message)

            LOGGER.error(error_msg, user.username, reason)
        return

    LOGGER.info('Noosfero user\'s basic info "%s" updated', user.username)

@receiver(delete_user)
def delete_user(sender, **kwargs):
    user = kwargs.get('user')

    noosfero_user = NoosferoUser.objects.filter(username=user.username).first()

    if not noosfero_user:
        return

    app_config = settings.COLAB_APPS.get('colab_noosfero', {})
    upstream = app_config.get('upstream', '').rstrip('/')
    verify_ssl = app_config.get('verify_ssl', True)

    users_endpoint = '{}/api/v1/profiles/{}'.format(upstream, noosfero_user.id)

    params = {
        'id': noosfero_user.id,
    }

    error_msg = u'Error trying to delete the user "%s" from Noosfero. Reason: %s'

    try:
        headers = {'Remote-User': user.username}
        response = requests.delete(users_endpoint, params=params,
                                 verify=verify_ssl, headers=headers)

    except Exception as excpt:
        reason = 'Request to API failed ({})'.format(excpt)
        LOGGER.error(error_msg, user.username, reason)
        return

    if response.status_code != 201:
        reason = 'Unknown.'

        try:
            fail_data = response.json()

        except ValueError as value_error:
            reason = '{} :: {}'.format(response.status_code,
                                       value_error.message)

            LOGGER.error(error_msg, user.username, reason)
        LOGGER.error(error_msg, user.username, fail_data)
        return

    LOGGER.info('Noosfero user "%s" deleted', user.username)
