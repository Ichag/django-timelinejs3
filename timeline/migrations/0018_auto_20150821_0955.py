# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0017_auto_20150820_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='options',
            field=models.ForeignKey(null=True, to='timeline.Options', related_name='option', blank=True, related_query_name='option'),
        ),
    ]
