# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 05:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0023_auto_20170905_1113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='c_address',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='c_city',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='c_first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='c_last_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='c_state',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='c_zip_code',
        ),
    ]
