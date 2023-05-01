# Generated by Django 4.0.4 on 2023-04-21 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contestants', '0021_newpageantregistration_is_in_agency'),
        ('voters', '0004_newslettersubscriber_alter_votepurchase_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votepurchase',
            name='contestant_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contestants.newpageantregistration'),
        ),
    ]
