# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-06 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='weight',
            field=models.IntegerField(null=True),
        ),
    ]
