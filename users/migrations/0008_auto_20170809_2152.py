# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-10 01:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20170809_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weight',
            name='user',
        ),
        migrations.DeleteModel(
            name='Weight',
        ),
    ]
