# Generated by Django 3.2 on 2021-09-27 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, unique=True)),
            ],
            options={
                'db_table': 'article_category1',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.AlterModelTable(
            name='comment',
            table=None,
        ),
        migrations.AlterModelTable(
            name='post',
            table=None,
        ),
    ]
