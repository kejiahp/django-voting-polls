# Generated by Django 4.0.4 on 2022-05-18 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contestants', '0014_registercontestant_is_evicted'),
        ('voters', '0002_votepurchase_amount_votepurchase_contestant_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votepurchase',
            name='contestant_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contestants.registercontestant'),
        ),
    ]