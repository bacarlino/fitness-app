# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-29 19:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20170729_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='sets',
        ),
        migrations.AddField(
            model_name='set',
            name='workout',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='tracker.Workout'),
        ),
    ]
