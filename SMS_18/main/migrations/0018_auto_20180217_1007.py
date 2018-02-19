# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20180216_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='time_of_post',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 17, 10, 7, 16, 813559), blank=True),
        ),
    ]
