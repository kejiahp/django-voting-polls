# Generated by Django 4.0.4 on 2023-04-21 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contestants', '0022_delete_registercontestant_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newpageantregistration',
            options={'ordering': ('-number_of_votes',), 'verbose_name': 'Pagaentry Registration', 'verbose_name_plural': 'Pagaentry Registrations'},
        ),
    ]