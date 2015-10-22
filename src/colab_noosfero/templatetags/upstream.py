from django import template
from django.conf import settings

register = template.Library()

@register.assignment_tag
def get_upstream():
    return settings.COLAB_APPS['colab_noosfero']['upstream'][:-1]

@register.assignment_tag
def get_default_image_url():
    return get_upstream()+"/images/icons-app/community-thumb.png"

@register.assignment_tag
def get_image_link_url(link):
    if not link:
        return get_default_image_url
    return get_upstream()+link
