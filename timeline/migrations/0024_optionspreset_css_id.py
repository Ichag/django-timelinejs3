# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0023_optionspreset_ease'),
    ]

    operations = [
        migrations.AddField(
            model_name='optionspreset',
            name='css_id',
            field=models.CharField(max_length=255, default='timeline-embed'),
        ),
    ]
