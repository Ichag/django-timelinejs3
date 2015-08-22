# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0018_auto_20150821_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='options',
            field=models.ForeignKey(to='timeline.Options', null=True, blank=True),
        ),
    ]
