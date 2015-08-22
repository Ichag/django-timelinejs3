# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0020_auto_20150821_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='OptionsPreset',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('preset_title', models.CharField(default='', max_length=255)),
                ('script_path', models.CharField(default='', max_length=255, blank=True)),
                ('height', models.IntegerField(default=0, blank=True)),
                ('width', models.IntegerField(default=0, blank=True)),
                ('scale_factor', models.IntegerField(default=3, blank=True, null=True)),
                ('layout', models.CharField(default='landscape', max_length=255, blank=True)),
                ('timenav_position', models.CharField(default='bottom', max_length=6, choices=[('top', 'Top'), ('bottom', 'Bottom')], blank=True)),
                ('optimal_tick_width', models.IntegerField(default=100, blank=True, null=True)),
                ('base_class', models.CharField(default='', max_length=255, blank=True)),
                ('timenav_height', models.IntegerField(default=150, blank=True, null=True)),
                ('timenav_height_percentage', models.IntegerField(default=25, blank=True, null=True)),
                ('timenav_height_min', models.IntegerField(default=150, blank=True, null=True)),
                ('marker_height_min', models.IntegerField(default=30, blank=True, null=True)),
                ('marker_width_min', models.IntegerField(default=100, blank=True, null=True)),
                ('marker_padding', models.IntegerField(default=5, blank=True, null=True)),
                ('start_at_slide', models.IntegerField(default=0, blank=True, null=True)),
                ('menubar_height', models.IntegerField(default=0, blank=True, null=True)),
                ('skinny_size', models.IntegerField(default=650, blank=True, null=True)),
                ('relative_date', models.BooleanField(default=False)),
                ('use_bc', models.BooleanField(default=False)),
                ('duration', models.IntegerField(default=1000, blank=True, null=True)),
                ('dragging', models.BooleanField(default=True)),
                ('trackResize', models.BooleanField(default=True)),
                ('map_type', models.CharField(default='stamen:toner-lite', max_length=255, blank=True)),
                ('slide_padding_lr', models.IntegerField(default=100, blank=True, null=True)),
                ('slide_default_fade', models.IntegerField(default=0, blank=True, null=True)),
                ('api_key_flickr', models.CharField(default='', max_length=255, blank=True)),
                ('language', models.CharField(default='en', max_length=255, blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Options',
        ),
        migrations.RemoveField(
            model_name='timeline',
            name='api_key_flickr',
        ),
        migrations.RemoveField(
            model_name='timeline',
            name='base_class',
        ),
        migrations.RemoveField(
            model_name='timeline',
            name='dragging',
        ),
        migrations.RemoveField(
            model_name='timeline',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='timeline',
            name='height',
        ),
        migrations.RemoveField(
            model_name='timeline',
            name='language',
        ),
        migrations.RemoveField(
            model_name='timeline',
            name='layout',
        ),
        migrations.RemoveField(
            model_name='timeline',
            name='map_type',
        ),
        migrations.RemoveField(
            model_name='timeline',
            name='marker_height_min',
        ),
        migrations.RemoveField(
            model_name='timeline',
            name='marker_padding',
        ),
        migrations.RemoveField(
            model_name='timeline',
            name='marker_width_min',
        ),
        migrations.RemoveField(
            model_name='timeline',
            name='menubar_height',
        ),
        migrations.RemoveField(
            model_name='timeline',
            name='optimal_tick_width',
        ),
        migrations.RemoveField(
            model_name='timeline',
            name='relative_date',
        ),
        migrations.RemoveField(
            model_name='timeline',
            name='scale_factor',
        ),
        migrations.RemoveField(
            model_name='timeline',
            name='script_path',
        ),
        migrations.RemoveField(
            model_name='timeline',
            name='skinny_size',
        ),
        migrations.RemoveField(
            model_name='timeline',
            name='slide_default_fade',
        ),
        migrations.RemoveField(
            model_name='timeline',
            name='slide_padding_lr',
        ),
        migrations.RemoveField(
            model_name='timeline',
            name='start_at_slide',
        ),
        migrations.RemoveField(
            model_name='timeline',
            name='timenav_height',
        ),
        migrations.RemoveField(
            model_name='timeline',
            name='timenav_height_min',
        ),
        migrations.RemoveField(
            model_name='timeline',
            name='timenav_height_percentage',
        ),
        migrations.RemoveField(
            model_name='timeline',
            name='timenav_position',
        ),
        migrations.RemoveField(
            model_name='timeline',
            name='trackResize',
        ),
        migrations.RemoveField(
            model_name='timeline',
            name='use_bc',
        ),
        migrations.RemoveField(
            model_name='timeline',
            name='width',
        ),
        migrations.AddField(
            model_name='timeline',
            name='options_preset',
            field=models.ForeignKey(null=True, blank=True, to='timeline.OptionsPreset', verbose_name='the related option set'),
        ),
    ]
