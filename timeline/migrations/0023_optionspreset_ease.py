# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0022_auto_20150822_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='optionspreset',
            name='ease',
            field=models.CharField(choices=[('easeInQuad', 'easeInQuad'), ('easeOutQuad', 'easeOutQuad'), ('easeInOutQuad', 'easeInOutQuad'), ('easeInCubic', 'easeInCubic'), ('easeOutCubic', 'easeOutCubic'), ('easeInOutCubic', 'easeInOutCubic'), ('easeInQuart', 'easeInQuart'), ('easeOutQuart', 'easeOutQuart'), ('easeInQuint', 'easeInQuint'), ('easeOutQuint', 'easeOutQuint'), ('easeInOutQuint', 'easeInOutQuint')], default='easeInOutQuint', max_length=255),
        ),
    ]
