# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-17 14:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0002_mag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cateria', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('descripcion', models.CharField(max_length=100)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturas.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('familia', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='categoria',
            name='familia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturas.Familia'),
        ),
    ]