# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-19 12:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20180216_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameswitch',
            name='game_status',
            field=models.IntegerField(choices=[('before_start', 'before_start'), ('live', 'live'), ('closed', 'closed')], default='before_start'),
        ),
        migrations.AlterField(
            model_name='newspost',
            name='time_of_post',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 2, 19, 18, 22, 8, 194227)),
        ),
    ]