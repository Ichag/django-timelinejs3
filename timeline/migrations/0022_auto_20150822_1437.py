# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0021_auto_20150822_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(verbose_name='Title', default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='optionspreset',
            name='layout',
            field=models.CharField(blank=True, choices=[('landscape', 'Landscape'), ('portrait', 'Portrait')], default='landscape', max_length=9),
        ),
    ]
