# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colab_noosfero', '0008_noosferosoftwareadmin_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoosferoComment',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('body', models.TextField(null=True, blank=True)),
                ('username', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(blank=True)),
                ('article', models.ForeignKey(to='colab_noosfero.NoosferoArticle')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
