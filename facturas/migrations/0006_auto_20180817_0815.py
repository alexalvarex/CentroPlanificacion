# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-17 14:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0005_auto_20180817_0812'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='cateria',
            new_name='categoria',
        ),
    ]
