# Generated by Django 4.0.3 on 2022-06-11 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blog_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default='lol', max_length=200),
            preserve_default=False,
        ),
    ]
