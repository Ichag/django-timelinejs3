# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0024_optionspreset_css_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeline',
            name='time_format',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='optionspreset',
            name='css_id',
            field=models.CharField(verbose_name='CSS ID for HTML Container', default='timeline-embed', max_length=255),
        ),
        migrations.AlterField(
            model_name='optionspreset',
            name='height',
            field=models.IntegerField(verbose_name='Container Height', default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='optionspreset',
            name='layout',
            field=models.CharField(choices=[('landscape', 'Landscape'), ('portrait', 'Portrait')], verbose_name='Orientation', default='landscape', blank=True, max_length=9),
        ),
        migrations.AlterField(
            model_name='optionspreset',
            name='preset_title',
            field=models.CharField(verbose_name='Preset Title', default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='optionspreset',
            name='scale_factor',
            field=models.IntegerField(help_text='How many screen widths wide should the timeline be', verbose_name='Scale factor', default=3, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='optionspreset',
            name='script_path',
            field=models.CharField(verbose_name='Path to TimelineJs Javascript File', default='', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='optionspreset',
            name='timenav_position',
            field=models.CharField(choices=[('top', 'Top'), ('bottom', 'Bottom')], verbose_name='Position of the Navigation', default='bottom', blank=True, max_length=6),
        ),
        migrations.AlterField(
            model_name='optionspreset',
            name='width',
            field=models.IntegerField(verbose_name='Container Width', default=0, blank=True),
        ),
    ]
