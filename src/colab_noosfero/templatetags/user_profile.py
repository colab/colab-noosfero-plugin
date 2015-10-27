from django import template
from django.core.urlresolvers import reverse


register = template.Library()


@register.simple_tag(takes_context=True)
def profile_url(context, username):
    if not username:
        return ""

    html = '- <a href="%s">%s</a>' % (reverse('user_profile',
                                              kwargs={'username': username}),
                                      username)
    return html
