# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-04 11:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20170313_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='u_processing_date_till',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 4, 11, 11, 52, 38, 85500, tzinfo=utc), null=True, verbose_name='Processing till date'),
        ),
    ]
