# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 04:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0024_auto_20170819_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shareselection',
            name='date',
            field=models.DateField(auto_now=True, null=True, verbose_name='Date Time'),
        ),
    ]
