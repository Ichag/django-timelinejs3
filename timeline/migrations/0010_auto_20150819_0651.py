# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0009_auto_20150819_0648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='options',
            name='script_path',
            field=models.CharField(default='', blank=True, max_length='255'),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='title',
            field=models.CharField(max_length='255'),
        ),
    ]
