# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-06 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central', '0004_auto_20180801_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acceso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_bodega', models.BooleanField(default=False)),
                ('is_planificador', models.BooleanField(default=False)),
                ('is_factura', models.BooleanField(default=False)),
                ('is_papeleria', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='colaborador',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='colaborador',
            name='is_bodega',
        ),
        migrations.RemoveField(
            model_name='colaborador',
            name='is_factura',
        ),
        migrations.RemoveField(
            model_name='colaborador',
            name='is_papeleria',
        ),
        migrations.RemoveField(
            model_name='colaborador',
            name='is_planificador',
        ),
    ]
