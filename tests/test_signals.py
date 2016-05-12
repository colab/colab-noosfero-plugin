from mock import Mock, patch

from django.test import TestCase, Client

from colab_noosfero.models import NoosferoUser
from colab_noosfero.signals import (update_basic_info_noosfero_user,
                                    delete_user)


class NoosferoTest(TestCase):

    def setUp(self):
        self.client = Client()

        super(NoosferoTest, self).setUp()

    @patch('colab_noosfero.signals.settings.COLAB_APPS')
    @patch('colab_noosfero.signals.requests.post')
    @patch('colab_noosfero.signals.LOGGER.info')
    def test_update_user_with_valid_remote_user(self, LOGGER_info_mock,
                                                resquests_post_mock,
                                                COLAB_APPS_mock):

        resquests_post_mock.return_value = Mock(
            status_code=201,
            json=lambda: {'message': 'Unauthorized'}
        )

        COLAB_APPS_mock.return_value = {
            'colab_noosfero': {
                'private_token': "TestToken",
                'upstream': "https://testeurl.com/",
                'verify_ssl': True,
            },
        }

        user = Mock(
            email="mail@mail.com",
            username="testuser",
            get_full_name=lambda: "Full Name Test"
        )
        NoosferoUser.objects.get_or_create(id=1, username="testuser")

        update_basic_info_noosfero_user(None, user=user, password="password")

        msg = ('Noosfero user\'s basic info "%s" updated')
        LOGGER_info_mock.assert_called_with(msg, user.username)

    @patch('colab_noosfero.signals.settings.COLAB_APPS')
    @patch('colab_noosfero.signals.requests.post')
    @patch('colab_noosfero.signals.LOGGER.error')
    def test_update_user_with_invalid_request(self, LOGGER_error_mock,
                                              resquests_post_mock,
                                              COLAB_APPS_mock):
        resquests_post_mock.side_effect = Exception()

        COLAB_APPS_mock.return_value = {
            'colab_noosfero': {
                'private_token': "TestToken",
                'upstream': "https://testeurl.com/",
                'verify_ssl': True,
            },
        }

        user = Mock(
            email="mail@mail.com",
            username="testuser",
            get_full_name=lambda: "Full Name Test"
        )

        NoosferoUser.objects.get_or_create(id=1, username="testuser")

        update_basic_info_noosfero_user(None, user=user)

        error_msg = u'Error trying to update "{}"\'s '
        error_msg += u'basic info on Noosfero. Reason: {}'
        reason = 'Request to API failed ({})'.format(Exception())

        error_msg = error_msg.format(user.username, reason)
        LOGGER_error_mock.assert_called_with(error_msg)

    def return_json(self):
        return {'message': 'Unauthorized'}

    @patch('colab_noosfero.signals.settings.COLAB_APPS')
    @patch('colab_noosfero.signals.requests.post')
    @patch('colab_noosfero.signals.LOGGER.error')
    def test_update_user_with_invalid_remote_user(self, LOGGER_error_mock,
                                                  resquests_post_mock,
                                                  COLAB_APPS_mock):

        json_resulted = self.return_json
        resquests_post_mock.return_value = Mock(
            status_code=500,
            json=self.return_json
        )

        COLAB_APPS_mock.return_value = {
            'colab_noosfero': {
                'upstream': "https://testeurl.com/",
                'verify_ssl': True,
            },
        }

        user = Mock(
            email="mail@mail.com",
            username="testuser",
            get_full_name=lambda: "Full Name Test"
        )

        NoosferoUser.objects.get_or_create(id=1, username="testuser")

        update_basic_info_noosfero_user(None, user=user)

        error_msg = u'Error trying to update "{}"\'s '
        error_msg += u'basic info on Noosfero. Reason: {}. JSON={}'
        error_msg = error_msg.format(user.username, 'Unknown', json_resulted())
        LOGGER_error_mock.assert_called_with(error_msg)

    @patch('colab_noosfero.signals.settings.COLAB_APPS')
    @patch('colab_noosfero.signals.requests.delete')
    @patch('colab_noosfero.signals.LOGGER.info')
    def test_delete_user_with_valid_remote_user(self, LOGGER_info_mock,
                                                resquests_post_mock,
                                                COLAB_APPS_mock):

        resquests_post_mock.return_value = Mock(
            status_code=200,
            json=lambda: {'message': 'Unauthorized'}
        )

        COLAB_APPS_mock.return_value = {
            'colab_noosfero': {
                'private_token': "TestToken",
                'upstream': "https://testeurl.com/",
                'verify_ssl': True,
            },
        }

        user = Mock(
            email="mail@mail.com",
            username="testuser",
            get_full_name=lambda: "Full Name Test"
        )

        NoosferoUser.objects.get_or_create(id=1, username="testuser")

        delete_user(None, user=user)

        msg = 'Noosfero user "{}" deleted'.format(user.username)
        LOGGER_info_mock.assert_called_with(msg)
        self.assertEquals(0, len(NoosferoUser.objects.filter(id=1)))

    @patch('colab_noosfero.signals.settings.COLAB_APPS')
    @patch('colab_noosfero.signals.requests.delete')
    @patch('colab_noosfero.signals.LOGGER.error')
    def test_delete_user_with_invalid_request(self, LOGGER_error_mock,
                                              resquests_post_mock,
                                              COLAB_APPS_mock):
        resquests_post_mock.side_effect = Exception()

        COLAB_APPS_mock.return_value = {
            'colab_noosfero': {
                'private_token': "TestToken",
                'upstream': "https://testeurl.com/",
                'verify_ssl': True,
            },
        }

        user = Mock(
            email="mail@mail.com",
            username="testuser",
            get_full_name=lambda: "Full Name Test"
        )

        NoosferoUser.objects.get_or_create(id=1, username="testuser")

        delete_user(None, user=user)

        error_msg = u'Error trying to delete the user "{}" '
        error_msg += u'on Noosfero. Reason: {}'
        reason = 'Request to API failed ({})'.format(Exception())
        error_msg = error_msg.format(user.username, reason)
        LOGGER_error_mock.assert_called_with(error_msg)

    @patch('colab_noosfero.signals.settings.COLAB_APPS')
    @patch('colab_noosfero.signals.requests.delete')
    @patch('colab_noosfero.signals.LOGGER.error')
    def test_delete_user_with_invalid_remote_user(self, LOGGER_error_mock,
                                                  resquests_post_mock,
                                                  COLAB_APPS_mock):

        json_resulted = self.return_json
        resquests_post_mock.return_value = Mock(
            status_code=500,
            json=self.return_json
        )

        COLAB_APPS_mock.return_value = {
            'colab_noosfero': {
                'upstream': "https://testeurl.com/",
                'verify_ssl': True,
            },
        }

        user = Mock(
            email="mail@mail.com",
            username="testuser",
            get_full_name=lambda: "Full Name Test"
        )

        NoosferoUser.objects.get_or_create(id=1, username="testuser")

        delete_user(None, user=user)

        error_msg = u'Error trying to delete the user "{}" on Noosfero.'
        error_msg += u' Reason: {}. JSON={}'
        error_msg = error_msg.format(user.username, 'Unknown', json_resulted())
        LOGGER_error_mock.assert_called_with(error_msg)
