
from django.conf import settings

from colab.plugins.views import ColabProxyView
from colab_spb.models import CommunityAssociations


class NoosferoProxyView(ColabProxyView):
    app_label = 'colab_noosfero'
    diazo_theme_template = 'proxy/noosfero.html'
    rewrite = (
        ('^/social/account/login(.*)$', r'{}\1'.format(settings.LOGIN_URL)),
    )
    
    def dispatch(self, request, *args, **kwargs):
        return super(NoosferoProxyView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(NoosferoProxyView, self).get_context_data(**kwargs)

        community = self.get_community_name(self.request.path)

        if not community:
            return

        associations = CommunityAssociations.objects.all()

        for community_association in associations:
            if community_association.community.name in community:
                context['community_association'] = {
                    'community': community_association.community.name,
                    'repository': community_association.group.url,
                    'mailman_list': community_association.mail_list.name,
                    'list_limit': 7,
                    'activities_limit': 7,
                }
                break             

        return context

    def get_community_name(self, path):
        community = None
        words = self.request.path.split('/')

        for index in range(len(words)):
                if 'profile' in words[index]:
                    community = words[index+1]
                    break

        return community
