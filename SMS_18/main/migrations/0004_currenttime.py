# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-21 10:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_stock_stocks_sold'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
