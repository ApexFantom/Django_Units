# Generated by Django 4.1.7 on 2023-04-17 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0004_customuser_alter_unitsdb_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='unitsdb',
            name='short_des',
            field=models.TextField(default='', verbose_name='Краткое описание'),
        ),
    ]
