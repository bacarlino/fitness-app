# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-08 01:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20170807_2107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='height',
            new_name='height_feet',
        ),
        migrations.AddField(
            model_name='profile',
            name='height_inches',
            field=models.IntegerField(null=True),
        ),
    ]
