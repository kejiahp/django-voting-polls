# Generated by Django 4.0.4 on 2023-02-03 10:14

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contestants', '0016_registercontestant_is_confirmed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registercontestant',
            name='image1',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='registercontestant',
            name='image2',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
