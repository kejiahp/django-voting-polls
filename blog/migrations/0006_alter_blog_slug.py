# Generated by Django 4.0.3 on 2022-06-11 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
