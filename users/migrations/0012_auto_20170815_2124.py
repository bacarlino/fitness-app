# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-16 02:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20170815_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='current_weight',
            field=models.DecimalField(decimal_places=1, max_digits=6, null=True),
        ),
    ]
