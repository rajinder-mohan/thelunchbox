# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 05:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0022_auto_20170831_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lunchbox',
            name='useless_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lunchbox',
            name='useless_time',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]