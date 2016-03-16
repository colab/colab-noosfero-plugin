from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from colab_noosfero.views import NoosferoProxyView, NoosferoProfileProxyView
from colab.widgets.widget_manager import Widget
import re
from django.utils.safestring import mark_safe

class NoosferoProfileWidget(NoosferoProxyView, Widget):
    identifier = 'noosfero_profile'
    name = _('Social')
    colab_form = None

    def default_url(self):
        return '/social/myprofile/macartur/profile_editor/edit'

    def fix_url(self, url):
        return re.sub('^.*/social/', '', url)

    def is_colab_form(self, request):
        if self.colab_form is None:
            self.colab_form = request.POST.get('colab_form', False)
        return self.colab_form

    def must_respond(self, request):
        return not self.is_colab_form(request) and '/social' in request.GET.get('path','')

    def dispatch(self, request, url):
        noosfero_proxy_view = NoosferoProfileProxyView()
        response = noosfero_proxy_view.dispatch(request, url)

        if response.status_code == 302:
            url = self.fix_url(self.default_url())
            request.method = 'GET'
            response = noosfero_proxy_view.dispatch(request, url)

        return response

    def change_request_method(self, request):
        if not self.must_respond(request):
            request.method = "GET"
        else:
            request.method = "POST"

    def requested_url(self, request):
        url = request.GET.get('path', '')

        if not url or not self.must_respond(request):
            url = self.default_url()

        return self.fix_url(url)

    def generate_content(self, **kwargs):
        request = kwargs.get('context', {}).get('request', None)
        self.change_request_method(request)
        response = self.dispatch(request, self.requested_url(request))

        if hasattr(response, 'content'):
            self.content = response.content
        else:
            self.content = "".join(response.streaming_content)
