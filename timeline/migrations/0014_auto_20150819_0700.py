# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0013_auto_20150819_0659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
