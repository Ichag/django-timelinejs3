# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0019_auto_20150821_1032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='options',
            name='api_key_flickr',
        ),
        migrations.RemoveField(
            model_name='options',
            name='base_class',
        ),
        migrations.RemoveField(
            model_name='options',
            name='dragging',
        ),
        migrations.RemoveField(
            model_name='options',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='options',
            name='height',
        ),
        migrations.RemoveField(
            model_name='options',
            name='language',
        ),
        migrations.RemoveField(
            model_name='options',
            name='layout',
        ),
        migrations.RemoveField(
            model_name='options',
            name='map_type',
        ),
        migrations.RemoveField(
            model_name='options',
            name='marker_height_min',
        ),
        migrations.RemoveField(
            model_name='options',
            name='marker_padding',
        ),
        migrations.RemoveField(
            model_name='options',
            name='marker_width_min',
        ),
        migrations.RemoveField(
            model_name='options',
            name='menubar_height',
        ),
        migrations.RemoveField(
            model_name='options',
            name='optimal_tick_width',
        ),
        migrations.RemoveField(
            model_name='options',
            name='preset_title',
        ),
        migrations.RemoveField(
            model_name='options',
            name='relative_date',
        ),
        migrations.RemoveField(
            model_name='options',
            name='scale_factor',
        ),
        migrations.RemoveField(
            model_name='options',
            name='script_path',
        ),
        migrations.RemoveField(
            model_name='options',
            name='skinny_size',
        ),
        migrations.RemoveField(
            model_name='options',
            name='slide_default_fade',
        ),
        migrations.RemoveField(
            model_name='options',
            name='slide_padding_lr',
        ),
        migrations.RemoveField(
            model_name='options',
            name='start_at_slide',
        ),
        migrations.RemoveField(
            model_name='options',
            name='timenav_height',
        ),
        migrations.RemoveField(
            model_name='options',
            name='timenav_height_min',
        ),
        migrations.RemoveField(
            model_name='options',
            name='timenav_height_percentage',
        ),
        migrations.RemoveField(
            model_name='options',
            name='timenav_position',
        ),
        migrations.RemoveField(
            model_name='options',
            name='trackResize',
        ),
        migrations.RemoveField(
            model_name='options',
            name='use_bc',
        ),
        migrations.RemoveField(
            model_name='options',
            name='width',
        ),
        migrations.RemoveField(
            model_name='timeline',
            name='options',
        ),
        migrations.AddField(
            model_name='timeline',
            name='api_key_flickr',
            field=models.CharField(default='', max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='timeline',
            name='base_class',
            field=models.CharField(default='', max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='timeline',
            name='dragging',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='timeline',
            name='duration',
            field=models.IntegerField(default=1000, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='timeline',
            name='height',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='timeline',
            name='language',
            field=models.CharField(default='en', max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='timeline',
            name='layout',
            field=models.CharField(default='landscape', max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='timeline',
            name='map_type',
            field=models.CharField(default='stamen:toner-lite', max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='timeline',
            name='marker_height_min',
            field=models.IntegerField(default=30, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='timeline',
            name='marker_padding',
            field=models.IntegerField(default=5, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='timeline',
            name='marker_width_min',
            field=models.IntegerField(default=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='timeline',
            name='menubar_height',
            field=models.IntegerField(default=0, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='timeline',
            name='optimal_tick_width',
            field=models.IntegerField(default=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='timeline',
            name='relative_date',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='timeline',
            name='scale_factor',
            field=models.IntegerField(default=3, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='timeline',
            name='script_path',
            field=models.CharField(default='', max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='timeline',
            name='skinny_size',
            field=models.IntegerField(default=650, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='timeline',
            name='slide_default_fade',
            field=models.IntegerField(default=0, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='timeline',
            name='slide_padding_lr',
            field=models.IntegerField(default=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='timeline',
            name='start_at_slide',
            field=models.IntegerField(default=0, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='timeline',
            name='timenav_height',
            field=models.IntegerField(default=150, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='timeline',
            name='timenav_height_min',
            field=models.IntegerField(default=150, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='timeline',
            name='timenav_height_percentage',
            field=models.IntegerField(default=25, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='timeline',
            name='timenav_position',
            field=models.CharField(default='bottom', max_length=6, blank=True, choices=[('top', 'Top'), ('bottom', 'Bottom')]),
        ),
        migrations.AddField(
            model_name='timeline',
            name='trackResize',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='timeline',
            name='use_bc',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='timeline',
            name='width',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
