# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colab_noosfero', '0005_auto_20151027_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='noosferoarticle',
            name='username',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='noosferocommunity',
            name='thumb_url',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
    ]
