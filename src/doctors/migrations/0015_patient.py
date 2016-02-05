# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-03 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0014_auto_20160203_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('num_street', models.IntegerField()),
                ('type_street', models.TextField()),
                ('name_street', models.TextField()),
                ('city', models.TextField(default='Champs-sur-Marne')),
                ('country', models.TextField(default='France')),
            ],
        ),
    ]
