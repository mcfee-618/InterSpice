# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2021-09-18 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, verbose_name='date published'),
        ),
    ]
