# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0012_auto_20150819_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='options',
            name='api_key_flickr',
            field=models.CharField(max_length=255, default='', blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='base_class',
            field=models.CharField(max_length=255, default='', blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='duration',
            field=models.IntegerField(null=True, blank=True, default=1000),
        ),
        migrations.AlterField(
            model_name='options',
            name='language',
            field=models.CharField(max_length=255, default='en', blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='layout',
            field=models.CharField(max_length=255, default='landscape', blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='map_type',
            field=models.CharField(max_length=255, default='stamen:toner-lite', blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='marker_height_min',
            field=models.IntegerField(null=True, blank=True, default=30),
        ),
        migrations.AlterField(
            model_name='options',
            name='marker_padding',
            field=models.IntegerField(null=True, blank=True, default=5),
        ),
        migrations.AlterField(
            model_name='options',
            name='marker_width_min',
            field=models.IntegerField(null=True, blank=True, default=100),
        ),
        migrations.AlterField(
            model_name='options',
            name='menubar_height',
            field=models.IntegerField(null=True, blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='options',
            name='optimal_tick_width',
            field=models.IntegerField(null=True, blank=True, default=100),
        ),
        migrations.AlterField(
            model_name='options',
            name='scale_factor',
            field=models.IntegerField(null=True, blank=True, default=3),
        ),
        migrations.AlterField(
            model_name='options',
            name='skinny_size',
            field=models.IntegerField(null=True, blank=True, default=650),
        ),
        migrations.AlterField(
            model_name='options',
            name='slide_default_fade',
            field=models.IntegerField(null=True, blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='options',
            name='slide_padding_lr',
            field=models.IntegerField(null=True, blank=True, default=100),
        ),
        migrations.AlterField(
            model_name='options',
            name='start_at_slide',
            field=models.IntegerField(null=True, blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='options',
            name='timenav_height',
            field=models.IntegerField(null=True, blank=True, default=150),
        ),
        migrations.AlterField(
            model_name='options',
            name='timenav_height_min',
            field=models.IntegerField(null=True, blank=True, default=150),
        ),
        migrations.AlterField(
            model_name='options',
            name='timenav_height_percentage',
            field=models.IntegerField(null=True, blank=True, default=25),
        ),
    ]
