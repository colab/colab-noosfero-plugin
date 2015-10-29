# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NoosferoArticle',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('path', models.CharField(max_length=255, null=True, blank=True)),
                ('body', models.TextField(null=True, blank=True)),
                ('profile_identifier', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(blank=True)),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NoosferoCategory',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NoosferoCommunity',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('identifier', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
                ('created_at', models.DateTimeField(blank=True)),
            ],
            options={
                'verbose_name': 'Community',
                'verbose_name_plural': 'Communities',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NoosferoSoftwareAdmin',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Noosfero Admin',
                'verbose_name_plural': 'Noosfero Admins',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='noosferocommunity',
            name='admins',
            field=models.ManyToManyField(to='colab_noosfero.NoosferoSoftwareAdmin'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='noosferocommunity',
            name='categories',
            field=models.ManyToManyField(to='colab_noosfero.NoosferoCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='noosferocommunity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='noosferoarticle',
            name='categories',
            field=models.ManyToManyField(to='colab_noosfero.NoosferoCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='noosferoarticle',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
