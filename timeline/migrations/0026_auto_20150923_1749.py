# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0025_auto_20150920_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='time_format',
            field=models.CharField(max_length=255, help_text='Time format for events like yyyy-mm-dd - H:m:y', default=''),
        ),
    ]
