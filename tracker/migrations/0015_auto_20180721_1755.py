# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-21 22:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0014_auto_20180721_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weight',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 21, 17, 55, 5, 10314)),
        ),
    ]
