from colab_noosfero.views import NoosferoProxyView
from urllib3.exceptions import MaxRetryError


def authenticate_user(sender, user, request, **kwargs):
    proxy_view = NoosferoProxyView()
    try:
        noosfero_response = proxy_view.dispatch(request, '/')
    except MaxRetryError:
        # Couldn't connect to noosfero
        return

    if noosfero_response.status_code == 200:
        request.COOKIES.set('_noosfero_session',
                            noosfero_response.cookies.get('_noosfero_session'))


def logout_user(sender, user, request, **kwargs):
    request.COOKIES.delete('_noosfero_session')
