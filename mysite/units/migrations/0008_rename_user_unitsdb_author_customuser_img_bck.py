# Generated by Django 4.1.7 on 2023-05-01 15:04

from django.db import migrations
import units.fields
import units.models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0007_unitsdb_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unitsdb',
            old_name='user',
            new_name='author',
        ),
        migrations.AddField(
            model_name='customuser',
            name='img_bck',
            field=units.fields.WEBPField(default='units/static/dist/img/no_image_big.png', upload_to=units.models.image_folder_avatar, verbose_name='Avatar'),
        ),
    ]
