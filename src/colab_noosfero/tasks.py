from urlparse import urljoin
from django.conf import settings
import requests
import json


def authenticate_user(sender, user, request, **kwargs):
    noosfero_settings = settings.COLAB_APPS.get('colab_noosfero')
    prefix = noosfero_settings.get('urls').get('prefix')
    prefix = prefix.replace('^', '')

    upstream = request.build_absolute_uri('/')
    url = urljoin(upstream, prefix)

    remote_user_data = {}
    remote_user_data['email'] = request.user.email
    remote_user_data['name'] = request.user.get_full_name()

    headers = {'HTTP_REMOTE_USER_DATA': json.dumps(
        remote_user_data, sort_keys=True)}

    noosfero_request = requests.get(url, headers=headers)
    request.COOKIES.set('_noosfero_session',
                        noosfero_request.cookies.get('_noosfero_session'))


def logout_user(sender, user, request, **kwargs):
    request.COOKIES.delete('_noosfero_session')
