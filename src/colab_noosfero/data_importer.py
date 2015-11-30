import json
import urllib
import urllib2
import logging

from dateutil.parser import parse

from django.db.models.fields import DateTimeField

from colab.plugins.data import PluginDataImporter

from .models import (NoosferoArticle, NoosferoCommunity,
                     NoosferoCategory, NoosferoSoftwareAdmin)

from colab.plugins.models import TimeStampPlugin

LOGGER = logging.getLogger('colab_noosfero')


class NoosferoDataImporter(PluginDataImporter):
    app_label = 'colab_noosfero'

    def get_request_url(self, path, **kwargs):
        upstream = self.config.get('upstream')
        kwargs['private_token'] = self.config.get('private_token')

        params = urllib.urlencode(kwargs)

        if upstream[-1] == '/':
            upstream = upstream[:-1]

        return u'{}{}?{}'.format(upstream, path, params)

    def get_json_data(self, api_url, page, per_page=1000, **kwargs):
        url = self.get_request_url(api_url, per_page=per_page, page=page,
                                   **kwargs)

        try:
            data = urllib2.urlopen(url, timeout=1000)
            print(url)
            json_data = json.load(data)
        except urllib2.URLError:
            LOGGER.exception("Connection timeout: " + url)
            json_data = []

        return json_data

    def fill_object_data(self, element, _object):
        for field in _object._meta.fields:
            try:
                if field.name == "user":
                    _object.update_user(
                        element["author"]["name"])
                    continue

                if field.name == "username":
                    _object.username = element["author"]["identifier"]

                if field.name == "profile_identifier":
                    _object.profile_identifier = \
                        element["profile"]["identifier"]
                    continue

                if isinstance(field, DateTimeField):
                    value = parse(element[field.name])
                else:
                    value = element[field.name]

                setattr(_object, field.name, value)
            except KeyError:
                continue
            except TypeError:
                continue

        return _object

    def fetch_communities(self):
        url = '/api/v1/communities'
        timestamp = TimeStampPlugin.get_last_updated('NoosferoCommunity')
        json_data = self.get_json_data(url, 1, timestamp=timestamp,
                                       order="updated_at ASC")

        if len(json_data) == 0:
            return

        json_data = json_data['communities']
        for element in json_data:
            community = NoosferoCommunity()
            self.fill_object_data(element, community)

            if element['image']:
                community.thumb_url = element['image']['thumb_url']
            community.save()

            if 'categories' in element:
                for category_json in element["categories"]:
                    category = NoosferoCategory.objects.get_or_create(
                        id=category_json["id"], name=category_json["name"])[0]
                    community.categories.add(category.id)

        self.save_last_update(json_data[-1]['updated_at'], 'NoosferoCommunity')

    def fetch_software_admins(self):
        url = '/api/v1/software_communities'
        timestamp = TimeStampPlugin.get_last_updated('NoosferoSoftwareAdmin')
        json_data = self.get_json_data(url, 1, timestamp=timestamp,
                                       order="updated_at ASC")

        if len(json_data) == 0:
            return

        json_data = json_data['softwares']
        for element in json_data:

            if not element['community']:
                continue

            software_name = element['community']['identifier']
            community = NoosferoCommunity.objects.filter(
                identifier=software_name).first()

            for admin in element['community']['admins']:
                instance = NoosferoSoftwareAdmin.objects.get_or_create(
                    id=admin['id'])[0]
                instance.name = admin['name']
                instance.save()
                community.admins.add(instance.id)

        self.save_last_update(json_data[-1]['community']['updated_at'],
                              'NoosferoSoftwareAdmin')

    def fetch_articles(self):
        url = '/api/v1/articles'
        timestamp = TimeStampPlugin.get_last_updated('NoosferoArticle')
        json_data = self.get_json_data(url, 1, timestamp=timestamp,
                                       order="updated_at ASC")

        if len(json_data) == 0:
            return

        json_data = json_data['articles']

        for element in json_data:
            article = NoosferoArticle()
            self.fill_object_data(element, article)
            article.save()

            for category_json in element["categories"]:
                category = NoosferoCategory.objects.get_or_create(
                    id=category_json["id"], name=category_json["name"])[0]
                article.categories.add(category.id)

        self.save_last_update(json_data[-1]['updated_at'], "NoosferoArticle")

    def save_last_update(self, last_updated, class_name):
        TimeStampPlugin.update_timestamp(class_name, last_updated=last_updated)

    def fetch_data(self):
        LOGGER.info("Importing Communities")
        self.fetch_communities()

        LOGGER.info("Importing Articles")
        self.fetch_articles()

        LOGGER.info("Importing Software Admins")
        self.fetch_software_admins()
