# Generated by Django 4.0.4 on 2023-04-21 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_delete_webhooktestmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newvotingwebhookmodel',
            options={'ordering': ('-amount',), 'verbose_name': 'Vote Payment', 'verbose_name_plural': 'Vote Payments'},
        ),
    ]