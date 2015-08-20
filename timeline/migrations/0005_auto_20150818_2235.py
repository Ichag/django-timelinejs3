# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0004_options_preset_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='options',
            name='timeline',
            field=models.ForeignKey(null=True, blank=True, to='timeline.Timeline'),
        ),
        migrations.AlterField(
            model_name='options',
            name='api_key_flickr',
            field=models.CharField(max_length='255', blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='base_class',
            field=models.CharField(max_length='255', blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='duration',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='height',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='language',
            field=models.CharField(max_length='255', blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='layout',
            field=models.CharField(max_length='255', blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='map_type',
            field=models.CharField(max_length='255', blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='marker_height_min',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='marker_padding',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='marker_width_min',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='menubar_height',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='optimal_tick_width',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='scale_factor',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='script_path',
            field=models.CharField(max_length='255', blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='skinny_size',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='slide_default_fade',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='slide_padding_lr',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='start_at_slide',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='timenav_height',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='timenav_height_min',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='timenav_height_percentage',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='timenav_position',
            field=models.CharField(max_length=6, blank=True, default='bottom', choices=[('top', 'Top'), ('bottom', 'Bottom')]),
        ),
        migrations.AlterField(
            model_name='options',
            name='width',
            field=models.IntegerField(blank=True),
        ),
    ]
