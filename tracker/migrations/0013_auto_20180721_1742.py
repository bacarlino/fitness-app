# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-21 22:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0012_auto_20170815_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weight',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 21, 17, 42, 32, 182173)),
        ),
    ]
