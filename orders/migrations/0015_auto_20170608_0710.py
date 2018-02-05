# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-08 05:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20170607_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='u_processing_date_till',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 6, 15, 5, 10, 0, 354908, tzinfo=utc), null=True, verbose_name=b'Processing till date'),
        ),
    ]