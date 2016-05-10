from mock import patch

from django.test import TestCase
from django.http import HttpRequest, HttpResponse, StreamingHttpResponse
from colab_noosfero.widgets.profile.profile import NoosferoProfileWidget
from colab_noosfero.views import NoosferoProfileProxyView
from colab.accounts.models import User


class WidgetsTest(TestCase):

    def setUp(self):
        self.profile_widget = NoosferoProfileWidget()
        self.current_request = HttpRequest()
        self.current_request.user = self.current_user()

        self.http_response = HttpResponse()
        self.streaming_http_response = StreamingHttpResponse()

    def current_user(self):
        return User(username='SampleUserTest')

    def test_default_url(self):
        url = "/social/myprofile/SampleUserTest/profile_editor/edit"
        result = self.profile_widget.default_url(self.current_request)
        self.assertEquals(result, url)

    @patch.object(NoosferoProfileProxyView, 'dispatch')
    def test_dispatch_with_redirect(self, dispatch_mock):
        self.http_response.status_code = 302

        content = '<head></head><body></body>'
        self.http_response.content = content

        dispatch_mock.return_value = self.http_response

        url = '/social/myprofile/test'
        result = self.profile_widget.dispatch(self.current_request, url)

        self.assertEquals(content, result.content)
        self.assertEquals(len(dispatch_mock.mock_calls), 2)

    @patch.object(NoosferoProfileProxyView, 'dispatch')
    def test_dispatch_without_redirect(self, dispatch_mock):
        self.http_response.status_code = 200
        self.http_response['Location'] = '/social/test'

        content = '<head></head><body></body>'
        self.http_response.content = content

        dispatch_mock.return_value = self.http_response

        url = '/social/myprofile/test'
        result = self.profile_widget.dispatch(self.current_request, url)

        self.assertEquals(content, result.content)
        self.assertEquals(len(dispatch_mock.mock_calls), 1)
