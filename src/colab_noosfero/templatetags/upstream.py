from django import template
from django.conf import settings

register = template.Library()

@register.filter
def get_upstream(value):
    return settings.COLAB_APPS['colab_noosfero']['upstream'][:-1]

@register.filter
def get_default_image_url(value):
    return get_upstream(value)+"/images/icons-app/community-thumb.png"
