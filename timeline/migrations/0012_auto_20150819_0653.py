# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0011_auto_20150819_0652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='options',
            name='api_key_flickr',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='base_class',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='language',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='layout',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='map_type',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='preset_title',
            field=models.CharField(max_length=255, default=''),
        ),
        migrations.AlterField(
            model_name='options',
            name='script_path',
            field=models.CharField(max_length=255, default='', blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='timenav_position',
            field=models.CharField(max_length=6, default='bottom', blank=True, choices=[('top', 'Top'), ('bottom', 'Bottom')]),
        ),
    ]
