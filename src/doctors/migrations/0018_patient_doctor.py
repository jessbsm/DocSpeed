# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-05 10:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0017_auto_20160203_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='doctors.Doctor'),
        ),
    ]
