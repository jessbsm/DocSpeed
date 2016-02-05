# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='address',
            field=models.TextField(default='new address'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='email',
            field=models.EmailField(default='new@email.com', max_length=250),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='fax',
            field=models.CharField(default='new fax number', max_length=10),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='name',
            field=models.CharField(default='new doctor', max_length=120),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phone',
            field=models.CharField(default='new phone number', max_length=10),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='photo',
            field=models.ImageField(default='/Users/jalelbenerrami/Desktop/hooray.jpg', upload_to=None),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='schedule',
            field=models.TextField(default='new schedule'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='site',
            field=models.URLField(default='www.newsite.com'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='speciality',
            field=models.TextField(default='new speciality'),
        ),
    ]
