# Generated by Django 4.0.4 on 2023-02-06 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contestants', '0018_remove_registercontestant_image2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registercontestant',
            name='instagram_handle',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='registercontestant',
            name='refnum',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
