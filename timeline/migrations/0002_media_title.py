# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title', default=''),
        ),
    ]
