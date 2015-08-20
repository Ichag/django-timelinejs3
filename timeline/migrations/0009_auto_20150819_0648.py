# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0008_auto_20150818_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='options',
            name='duration',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='height',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='marker_height_min',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='marker_padding',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='marker_width_min',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='menubar_height',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='optimal_tick_width',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='scale_factor',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='skinny_size',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='slide_default_fade',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='slide_padding_lr',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='start_at_slide',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='timenav_height',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='timenav_height_min',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='timenav_height_percentage',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='width',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
