# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-07 12:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0010_auto_20170706_0903'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name=b'Customer name')),
                ('address', models.CharField(max_length=255, null=True, verbose_name=b'Address')),
                ('street', models.CharField(max_length=255, null=True, verbose_name=b'Street')),
                ('city', models.CharField(default=b'Barcelona', max_length=50, null=True, verbose_name=b'City')),
                ('state', models.CharField(default=b'Catalonia', max_length=30, null=True, verbose_name=b'State full')),
                ('zip_code', models.CharField(max_length=10, null=True, verbose_name=b'Zip Code')),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='company',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.AddField(
            model_name='profile',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofiles.Customer', verbose_name=b'Customer'),
        ),
    ]
