# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-05 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, default='', max_length=50)),
                ('apellido', models.CharField(blank=True, default='', max_length=50)),
                ('telefono_fijo', models.CharField(blank=True, default='', max_length=30)),
                ('celular', models.CharField(blank=True, default='', max_length=30)),
                ('pais', models.CharField(blank=True, default='', max_length=30)),
                ('provincia', models.CharField(blank=True, default='', max_length=30)),
                ('ciudad', models.CharField(blank=True, default='', max_length=30)),
                ('calle', models.CharField(blank=True, default='', max_length=30)),
                ('altura', models.CharField(blank=True, default='', max_length=30)),
                ('entre_calle', models.CharField(blank=True, default='', max_length=30)),
                ('piso', models.CharField(blank=True, default='', max_length=30)),
                ('depto', models.CharField(blank=True, default='', max_length=30)),
                ('codigo_postal', models.CharField(blank=True, default='', max_length=30)),
                ('mail', models.CharField(blank=True, default='', max_length=30)),
                ('web', models.CharField(blank=True, default='', max_length=30)),
            ],
        ),
    ]
