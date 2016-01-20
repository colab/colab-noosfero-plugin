from urlparse import urljoin
import requests
import json


def authenticate_user(sender, user, request, **kwargs):
    upstream = request.build_absolute_uri().split('/account/login')[0]
    url = urljoin(upstream, 'social/')
    remote_user_data = {}

    remote_user_data['email'] = request.user.email
    remote_user_data['name'] = request.user.get_full_name()

    headers = {'HTTP_REMOTE_USER_DATA': json.dumps(
        remote_user_data, sort_keys=True)}

    request_noosfero = requests.get(url, headers=headers)
    request.COOKIES.set('_noosfero_session',
                        request_noosfero.cookies.get('_noosfero_session'))
