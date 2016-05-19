import os
import sys

from django.conf import settings
from django.shortcuts import redirect

from colab.plugins.views import ColabProxyView


class NoosferoProxyView(ColabProxyView):
    app_label = 'colab_noosfero'
    diazo_theme_template = 'proxy/noosfero.html'

    rewrite = (
        ('^/social/account/login(.*)$', r'{}\1'.format(settings.LOGIN_URL)),
        ('^/social/account/change_password$', 'password_change')
    )

    def verify_forbidden_path(self, path, user):
        forbidden = '/social/myprofile/{}/profile_editor/edit'.format(user)
        if forbidden in path:
            return True
        return False

    def dispatch(self, request, *args, **kwargs):
        self.request = request

        if self.verify_forbidden_path(self.request.path, self.request.user):
            tab = r'#noosfero_profile'
            path = r'/account/{}/edit'.format(self.request.user)
            return redirect(path+tab)

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


class NoosferoProfileProxyView(ColabProxyView):
    app_label = 'colab_noosfero'
    diazo_theme_template = 'widgets/noosfero_profile.html'

    @property
    def diazo_rules(self):
        child_class_file = sys.modules[self.__module__].__file__
        app_path = os.path.abspath(os.path.dirname(child_class_file))
        diazo_path = os.path.join(app_path, 'widgets/profile/diazo.xml')

        self.log.debug("diazo_rules: %s", diazo_path)
        return diazo_path
