# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0010_auto_20150819_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='options',
            name='timenav_position',
            field=models.CharField(choices=[('top', 'Top'), ('bottom', 'Bottom')], max_length='6', blank=True, default='bottom'),
        ),
    ]
