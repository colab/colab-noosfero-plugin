
from django.test import TestCase
from django.test.utils import override_settings

from colab_noosfero.data_importer import NoosferoDataImporter
from colab_noosfero.models import (NoosferoSoftwareAdmin, NoosferoCategory,
                                   NoosferoCommunity, NoosferoArticle)
import urllib
import data
from dateutil.parser import parse
from mock import patch


class NoosferoDataImporterTest(TestCase):

    @override_settings(COLAB_APPS=data.colab_apps)
    def setUp(self):
        self.api = NoosferoDataImporter()

    def test_resquest_url(self):
        url = self.api.get_request_url('/social/test/')
        expected = 'localhost/social/test/?private_token=token'
        self.assertEqual(url, expected)

    def test_resquest_url_with_params(self):
        url = self.api.get_request_url('/social/test/', param='param',
                                       timestamp='2015/25/10')
        expected = u'localhost/social/test/?timestamp=2015%2F25%2F10' \
        '&private_token=token&param=param'

        self.assertEqual(url, expected)

    @patch.object(NoosferoDataImporter, 'get_json_data')
    def test_fetch_community(self, mock_json):
        mock_json.side_effect = [data.community_json, []]

        communities = self.api.fetch_communities()
        size_communities = NoosferoCommunity.objects.count()
        self.assertEqual(size_communities, 2)

        community = NoosferoCommunity.objects.filter(
            identifier="software_test_community").first()
        self.assertEqual("Software Test Community",community.name)
        self.assertEqual(71,community.id)
        self.assertIsNone(community.description)

    @patch.object(NoosferoDataImporter, 'get_json_data')
    def test_fetch_articles(self, mock_json):
        mock_json.side_effect = [data.articles_json, []]

        articles= self.api.fetch_articles()
        size_articles= NoosferoArticle.objects.count()
        self.assertEqual(size_articles, 3)

        article = NoosferoArticle.objects.filter(
            title="Gallery").first()
        self.assertEqual(211,article.id)
        self.assertIsNone(article.body)

    @patch.object(NoosferoDataImporter, 'get_json_data')
    def test_fetch_software_admin(self, mock_json):
        mock_json.side_effect = [data.community_json, []]
        self.api.fetch_communities()

        community_id = 69
        community = NoosferoCommunity.objects.filter(id=community_id)[0]

        admins_json = filter(lambda community: community['id'] == community_id,
                             data.community_json['communities'])[0]
        admins_json = admins_json['admins']

        mock_json.side_effect = [admins_json, []]
        self.api.fetch_software_admins(community, admins_json)

        size_admins= NoosferoSoftwareAdmin.objects.count()
        self.assertEqual(size_admins, 2)

        admin = NoosferoSoftwareAdmin.objects.filter(
            id=68).first()
        self.assertEqual('admin admin',admin.name)
