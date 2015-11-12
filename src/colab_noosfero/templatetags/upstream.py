from django import template
from django.conf import settings
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

register = template.Library()


def get_upstream():
    return settings.COLAB_APPS['colab_noosfero']['upstream'][:-1]


def get_default_image_url(size):
    return get_upstream() + "/images/icons-app/community-{}.png".format(size)


@register.simple_tag()
def get_image_link_url(link, size):
    if not link:
        return get_default_image_url(size)
    return get_upstream() + link


@register.simple_tag()
def get_author(username):
    if username == '':
        return ''
    else:
        profile = reverse('user_profile', kwargs={'username': username})
        return _("By") + ' <a href="%s">%s</a>' % (profile, username)
