# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0005_auto_20150818_2235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='options',
            name='timeline',
        ),
        migrations.AddField(
            model_name='timeline',
            name='options',
            field=models.ForeignKey(blank=True, null=True, to='timeline.Options'),
        ),
    ]
