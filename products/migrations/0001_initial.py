# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-31 05:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('name', models.CharField(default=b'N/A', max_length=50)),
                ('productType', models.CharField(default=b'N/A', max_length=30)),
                ('brand', models.CharField(default=b'N/A', max_length=30)),
                ('price', models.FloatField(default=b'00.00')),
                ('productStock', models.IntegerField(default=b'0')),
                ('description', models.CharField(default=b'N/A', max_length=200)),
                ('year', models.IntegerField(default=b'0000')),
                ('variety', models.CharField(default=b'N/A', max_length=30)),
                ('origin', models.CharField(default=b'N/A', max_length=30)),
                ('maker', models.CharField(default=b'N/A', max_length=50)),
                ('size', models.FloatField(default=b'00.00')),
                ('codigo', models.CharField(default=b'', max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('estado', models.TextField(default=b'BO', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='VentaProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cant', models.IntegerField(default=b'0000')),
                ('precio', models.FloatField(default=b'00.00')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Venta')),
            ],
        ),
        migrations.AddField(
            model_name='venta',
            name='products',
            field=models.ManyToManyField(through='products.VentaProducto', to='products.Product'),
        ),
    ]