from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from colab_noosfero.views import NoosferoProxyView, NoosferoProfileProxyView
from colab.widgets.widget_manager import Widget
import re

class NoosferoProfileWidget(NoosferoProxyView, Widget):
    identifier = 'noosfero_profile'
    name = _('Social')

    def default_url(self):
        return '/myprofile/macartur/profile_editor/edit'

    def change_request_method(self, request):
        if not len(request.POST) or request.POST.get('colab_form', None):
            request.method = "GET"
        elif not request.POST.get("_method", None):
            request.method = "POST"
        else:
            request.method = request.POST.get("_method").upper()

    def generate_content(self, **kwargs):
        request = kwargs.get('context', {}).get('request', None)

        is_colab_form = request.POST.get('colab_form', False)
        path = request.GET.get('path', '')

        if is_colab_form or not path:
            requested_url = self.default_url()
        else:
            requested_url = path

        requested_url = self.fix_requested_url(requested_url)
        self.change_request_method(request)
        noosfero_proxy_view = NoosferoProfileProxyView()

        response = noosfero_proxy_view.dispatch(request, requested_url)

        if response.status_code == 302:
            requested_url = self.fix_requested_url(self.default_url())
            request.method = 'GET'
            response = noosfero_proxy_view.dispatch(request, requested_url)

        if hasattr(response, 'content'):
            self.content = response.content
        else:
            self.content = "".join(response.streaming_content)

    def fix_requested_url(self, url):
        return re.sub('^(.*)/social', '', url)
