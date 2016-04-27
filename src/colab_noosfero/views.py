
from django.conf import settings

from colab.plugins.views import ColabProxyView


class NoosferoProxyView(ColabProxyView):
    app_label = 'colab_noosfero'
    diazo_theme_template = 'proxy/noosfero.html'
    rewrite = (
        ('^/social/account/login(.*)$', r'{}\1'.format(settings.LOGIN_URL)),
        ('^/social/profile/([\w@+.-]+)$', r'/account/\1/edit'),
    )

    def dispatch(self, request, *args, **kwargs):
        return super(NoosferoProxyView, self).dispatch(request,
                                                       *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(NoosferoProxyView, self).get_context_data(**kwargs)

        community = self.get_community_name(self.request.path)

        if not community:
            return
        context['community'] = community
        return context

    def get_community_name(self, path):
        words = self.request.path.split('/')
        if not self.request.path.startswith('/social/profile'):
            return

        words = [word for word in words if word]
        return words[-1]

    def get_request_headers(self):
        headers = super(NoosferoProxyView, self).get_request_headers()
        headers['Host'] = self.request.META['HTTP_HOST']
        return headers
