# Generated by Django 4.0.4 on 2023-04-21 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voters', '0005_alter_votepurchase_contestant_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='VotePurchase',
        ),
    ]