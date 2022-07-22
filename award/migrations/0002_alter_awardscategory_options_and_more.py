# Generated by Django 4.0.4 on 2022-07-22 10:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='awardscategory',
            options={'verbose_name_plural': 'Awards categories'},
        ),
        migrations.AlterField(
            model_name='awardscontestant',
            name='image1',
            field=models.ImageField(default='defaultuser.jpg', upload_to='award/contestant/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='awardscontestant',
            name='image2',
            field=models.ImageField(default='defaultuser.jpg', upload_to='award/contestant/%Y/%m/%d'),
        ),
        migrations.CreateModel(
            name='AwardVotePurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('number_of_votes', models.IntegerField(default=0)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('verified', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('contestant_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='award.awardscontestant')),
            ],
            options={
                'ordering': ('-amount',),
            },
        ),
    ]
