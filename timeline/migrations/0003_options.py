# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0002_media_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('script_path', models.CharField(max_length='255')),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
                ('scale_factor', models.IntegerField()),
                ('layout', models.CharField(max_length='255')),
                ('timenav_position', models.CharField(max_length=6, default='bottom', choices=[('top', 'Top'), ('bottom', 'Bottom')])),
                ('optimal_tick_width', models.IntegerField()),
                ('base_class', models.CharField(max_length='255')),
                ('timenav_height', models.IntegerField()),
                ('timenav_height_percentage', models.IntegerField()),
                ('timenav_height_min', models.IntegerField()),
                ('marker_height_min', models.IntegerField()),
                ('marker_width_min', models.IntegerField()),
                ('marker_padding', models.IntegerField()),
                ('start_at_slide', models.IntegerField()),
                ('menubar_height', models.IntegerField()),
                ('skinny_size', models.IntegerField()),
                ('relative_date', models.BooleanField(default=False)),
                ('use_bc', models.BooleanField(default=False)),
                ('duration', models.IntegerField()),
                ('dragging', models.BooleanField(default=True)),
                ('trackResize', models.BooleanField(default=True)),
                ('map_type', models.CharField(max_length='255')),
                ('slide_padding_lr', models.IntegerField()),
                ('slide_default_fade', models.IntegerField()),
                ('api_key_flickr', models.CharField(max_length='255')),
                ('language', models.CharField(max_length='255')),
            ],
        ),
    ]
