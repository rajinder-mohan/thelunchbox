# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-07 13:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0052_auto_20170707_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='u_processing_date_till',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 7, 14, 13, 13, 21, 369046, tzinfo=utc), null=True, verbose_name=b'Processing till date'),
        ),
    ]
