# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appQRMusical', '0008_auto_20170815_1320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='image_width',
        ),
        migrations.AlterField(
            model_name='settings',
            name='image_height',
            field=models.IntegerField(default=240),
        ),
        migrations.AlterField(
            model_name='settings',
            name='timeout',
            field=models.IntegerField(default=2000),
        ),
    ]