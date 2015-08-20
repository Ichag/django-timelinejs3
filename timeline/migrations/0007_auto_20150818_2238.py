# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0006_auto_20150818_2235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeline',
            name='options',
        ),
        migrations.AddField(
            model_name='options',
            name='timeline',
            field=models.ForeignKey(to='timeline.Timeline', blank=True, null=True),
        ),
    ]
