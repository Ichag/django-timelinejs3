# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0014_auto_20150819_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='options',
            name='preset_title',
            field=models.CharField(default=' ', max_length=255),
        ),
    ]
