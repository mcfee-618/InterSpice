# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2021-09-18 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0003_auto_20210918_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='tag',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='source',
            field=models.IntegerField(default=0),
        ),
    ]
