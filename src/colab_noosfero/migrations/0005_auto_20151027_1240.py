# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colab_noosfero', '0004_noosferocommunity_thumb_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noosferocommunity',
            name='thumb_url',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
