# Generated by Django 4.0.4 on 2023-02-03 10:14

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0002_alter_awardscategory_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awardscontestant',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='awardscontestant',
            name='image1',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='awardscontestant',
            name='image2',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='awardscontestant',
            name='phonenumber',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]