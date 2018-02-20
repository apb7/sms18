# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20180217_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='time_of_post',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
    ]
