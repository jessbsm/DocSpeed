# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-05 10:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0022_remove_patient_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='doctors.Doctor'),
            preserve_default=False,
        ),
    ]
