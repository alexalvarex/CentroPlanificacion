# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-17 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0004_auto_20180817_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familia',
            name='familia',
            field=models.IntegerField(),
        ),
    ]