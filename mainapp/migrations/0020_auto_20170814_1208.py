# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_usernotification_head'),
    ]

    operations = [
        migrations.AddField(
            model_name='usernotification',
            name='head_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='usernotification',
            name='head_es',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='usernotification',
            name='msg_en',
            field=models.TextField(blank=True, null=True, verbose_name='Message'),
        ),
        migrations.AddField(
            model_name='usernotification',
            name='msg_es',
            field=models.TextField(blank=True, null=True, verbose_name='Message'),
        ),
    ]
