# Generated by Django 4.0.4 on 2023-04-19 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_alter_newvotingwebhookmodel_contestant_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='WebhookTestModel',
        ),
    ]
