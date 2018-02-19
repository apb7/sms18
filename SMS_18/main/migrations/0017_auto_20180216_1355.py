# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20180216_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='time_of_post',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 16, 13, 55, 32, 801868), blank=True),
        ),
    ]
