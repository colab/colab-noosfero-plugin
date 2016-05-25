from colab.settings import COLAB_APPS, SESSION_COOKIE_AGE
import requests
import logging
logger = logging.getLogger(__name__)


def get_upstream():
    return COLAB_APPS.get('colab_noosfero', '').get('upstream', '')


# TODO: need to use noosfero_proxy_view to make authentication,
# requests was used because Noosfero only send a _noosfero_session
# in the first request
def authenticate_user(sender, user, request, **kwargs):

    try:
        headers = {'REMOTE_USER': user.username}
        noosfero_response = requests.get(get_upstream(), headers=headers)
    except:
        logger.info("Couldn't connect to noosfero")
        return

    if noosfero_response.status_code == 200:
        session = noosfero_response.cookies.get('_noosfero_session')
        request.COOKIES.set('_noosfero_session', session,
                            expires=SESSION_COOKIE_AGE)


def logout_user(sender, user, request, **kwargs):
    request.COOKIES.delete('_noosfero_session')
