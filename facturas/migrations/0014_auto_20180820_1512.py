# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-20 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0013_familia_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familia',
            name='familia',
            field=models.CharField(max_length=100),
        ),
    ]
