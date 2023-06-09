# Generated by Django 4.1.7 on 2023-04-04 17:54

from django.db import migrations
import units.fields
import units.models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='unitsdb',
            name='img_bck',
            field=units.fields.WEBPField(default='units/static/dist/img/no_image_big.png', upload_to=units.models.image_folder_bck, verbose_name='ImageBck'),
        ),
        migrations.AlterField(
            model_name='unitsdb',
            name='img',
            field=units.fields.WEBPField(default='units/static/dist/img/no_image_big.png', upload_to=units.models.image_folder, verbose_name='ImageIcon'),
        ),
    ]
