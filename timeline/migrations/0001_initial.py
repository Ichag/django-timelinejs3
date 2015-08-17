# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255, verbose_name='internal Title')),
                ('start_date', models.DateTimeField(verbose_name='start_date')),
                ('end_date', models.DateTimeField(verbose_name='end_date')),
                ('slug', models.SlugField(default='', verbose_name='slug')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(null=True, default='', verbose_name='url')),
                ('caption', models.TextField(null=True, default='', blank=True, verbose_name='caption')),
                ('credit', models.TextField(null=True, default='', blank=True, verbose_name='credit')),
                ('thumbnail', models.URLField(null=True, default='', blank=True, verbose_name='thumbnail')),
                ('slug', models.SlugField(default='', verbose_name='slug')),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255, verbose_name='headline')),
                ('text', models.TextField(blank=True, verbose_name='text')),
                ('slug', models.SlugField(default='', verbose_name='slug')),
            ],
        ),
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('published', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(default='', verbose_name='slug')),
                ('media', models.OneToOneField(to='timeline.Media', null=True, blank=True)),
                ('text', models.OneToOneField(to='timeline.Text', null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='event',
            name='media',
            field=models.OneToOneField(to='timeline.Media', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='text',
            field=models.OneToOneField(to='timeline.Text', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='timeline',
            field=models.ForeignKey(to='timeline.Timeline'),
        ),
    ]
