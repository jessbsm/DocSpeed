# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-03 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0016_auto_20160203_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='doctor',
            name='longitude',
            field=models.FloatField(default=0),
        ),
    ]
