# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-17 21:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0008_ordeninterna'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden_trabajo', models.CharField(blank=True, max_length=100, null=True)),
                ('solped', models.CharField(blank=True, max_length=100, null=True)),
                ('orden_servico', models.CharField(max_length=100)),
                ('num_factura', models.IntegerField()),
                ('monto_lps', models.FloatField()),
                ('descripcion', models.CharField(max_length=100)),
                ('fecha_fac', models.DateField()),
                ('fecha_reg', models.DateField()),
                ('fecha_pago', models.DateField()),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturas.Equipo')),
                ('mag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturas.MAG')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturas.Proveedor')),
            ],
        ),
        migrations.RemoveField(
            model_name='ordeninterna',
            name='equipo',
        ),
        migrations.RemoveField(
            model_name='ordeninterna',
            name='mag',
        ),
        migrations.RemoveField(
            model_name='ordeninterna',
            name='proveedor',
        ),
        migrations.DeleteModel(
            name='OrdenInterna',
        ),
    ]
