# Generated by Django 3.2 on 2021-12-11 07:58

import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, unique=True)),
                ('introduction', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('cover', models.ImageField(null=True, upload_to='')),
                ('link', models.CharField(blank=True, max_length=100, unique=True)),
                ('status', models.IntegerField()),
                ('timestamp', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, unique=True)),
            ],
        ),
    ]