from colab_noosfero.views import NoosferoProxyView


def authenticate_user(sender, user, request, **kwargs):
    proxy_view = NoosferoProxyView()
    noosfero_request = proxy_view.dispatch(request, '/')

    if noosfero_request.status_code == 200:
        request.COOKIES.set('_noosfero_session',
                            noosfero_request.cookies.get('_noosfero_session'))


def logout_user(sender, user, request, **kwargs):
    request.COOKIES.delete('_noosfero_session')
