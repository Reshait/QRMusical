# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-01 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('filename', models.CharField(max_length=100)),
                ('resolution', models.CharField(max_length=10)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image_width', models.CharField(max_length=10)),
                ('image_height', models.CharField(max_length=10)),
                ('image_rotation', models.BooleanField(default=False)),
            ],
        ),
    ]
