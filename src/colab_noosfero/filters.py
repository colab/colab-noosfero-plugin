from django.utils.translation import ugettext as _

def get_filters(request):
    return {
        'noosfero_community': {
            'name': _(u'Communities'),
            'icon': 'globe',
            'fields': (
                ('title', _(u'Name'), request.GET.get('title')),
                (
                    'description',
                    _(u'Description'), 
                    request.GET.get('description'),
                ),
            ),
        },
        'noosfero_articles': {
            'name': _(u'Article'),
            'icon': 'list-alt',
            'fields': (
                ('title', _(u'Title'), request.GET.get('title')),
                (
                    'body',
                    _(u'Content'), 
                    request.GET.get('body'),
                ),
            ),
        },
    }
