# -*- coding: utf-8 -*-

import string

from haystack import indexes
from haystack.utils import log as logging

from .models import (NoosferoArticle, NoosferoCommunity)


logger = logging.getLogger('haystack')

# The string maketrans always return a string encoded with latin1
# http://stackoverflow.com/questions/1324067/how-do-i-get-str-translate-to-work-with-unicode-strings
table = string.maketrans(
    string.punctuation,
    '.' * len(string.punctuation)
).decode('latin1')


class NoosferoCommunityIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, stored=False)
    title = indexes.CharField(model_attr='name')
    description = indexes.CharField(model_attr='description', null=True)
    url = indexes.CharField(model_attr='url', indexed=False)
    icon_name = indexes.CharField()
    type = indexes.CharField()
    modified = indexes.DateTimeField(model_attr='modified', null=True)
    created_at = indexes.DateTimeField(model_attr='created_at', null=True)
    category = indexes.MultiValueField()
    thumb_url = indexes.CharField(model_attr='thumb_url', null=True)

    def prepare_category(self, obj):
        return obj.categories.values_list('name', flat=True)

    def prepare_icon_name(self, obj):
        return u'file'

    def get_ful_name(self):
        self.objs.name

    def get_model(self):
        return NoosferoCommunity

    def prepare_type(self, obj):
        return u'noosfero_community'


class NoosferoArticleIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField(document=True, use_template=True, stored=False)
    title = indexes.CharField(model_attr='title')
    username = indexes.CharField(model_attr='username', null=True)
    body = indexes.CharField(model_attr='body', null=True)
    url = indexes.CharField(model_attr='url', indexed=False)
    icon_name = indexes.CharField()
    type = indexes.CharField(model_attr='type')
    modified = indexes.DateTimeField(model_attr='modified', null=True)
    created_at = indexes.DateTimeField(model_attr='created_at', null=True)
    category = indexes.MultiValueField()

    def get_model(self):
        return NoosferoArticle

    def prepare_category(self, obj):
        return obj.categories.values_list('name', flat=True)

    def prepare_icon_name(self, obj):
        return u'file'

    def prepare_type(self, obj):
        return u'noosfero_articles'
