# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0016_auto_20150820_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='options',
            name='height',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='width',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
