# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-08 11:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_delete_paywallet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkoutcomment',
            name='user',
        ),
        migrations.DeleteModel(
            name='CheckoutComment',
        ),
    ]
