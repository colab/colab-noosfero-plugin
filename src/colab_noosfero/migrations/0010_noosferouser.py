# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colab_noosfero', '0009_noosferocomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoosferoUser',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Noosfero User',
                'verbose_name_plural': 'Noosfero User',
            },
            bases=(models.Model,),
        ),
    ]
