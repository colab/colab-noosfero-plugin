
from django.test import TestCase
from django.conf import settings

from colab_noosfero.models import (NoosferoArticle,
                                   NoosferoComment)


class NoosferoModelTest(TestCase):

    def test_comment(self):
        article = NoosferoArticle()
        article.profile_identifier = "profile"
        article.path = "url"
        article.title = "title"
        comment = NoosferoComment()
        comment.article = article
        url = u'/{prefix}/{profile}/{path}?view=true'.format(
                     prefix=self.get_prefix(),
                     profile=article.profile_identifier,
                     path=article.path)

        self.assertEqual(url, comment.url)
        self.assertEqual("title", comment.title)

    def get_prefix(self):
        return settings.COLAB_APPS['colab_noosfero']['urls']['prefix'][1:-1]
