# Generated by Django 4.0.4 on 2023-04-19 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0005_alter_awardscontestant_instagram_handle_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewAwardsRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=300)),
                ('lastname', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('category', models.CharField(choices=[('VIDEO DIRECTOR OF THE YEAR', 'VIDEO DIRECTOR OF THE YEAR'), ('PAGEANT ICON OF THE YEAR', 'PAGEANT ICON OF THE YEAR'), ('ARTISTE OF THE YEAR', 'ARTISTE OF THE YEAR'), ('MEDIA PERSONALITY OF THE YEAR', 'MEDIA PERSONALITY OF THE YEAR'), ('ENTREPRENEUR OF THE YEAR', 'ENTREPRENEUR OF THE YEAR'), ('CINEMATIC STAR OF THE YEAR', 'CINEMATIC STAR OF THE YEAR'), ('SONG / ARTISTE OF THE YEAR', 'SONG / ARTISTE OF THE YEAR'), ('BRAND OF THE YEAR', 'BRAND OF THE YEAR'), ('DANCER OF THE YEAR', 'DANCER OF THE YEAR'), ('MODEL OF THE YEAR OF THE YEAR', 'MODEL OF THE YEAR OF THE YEAR'), ('COMEDIAN / SKITMAKER OF THE YEAR', 'COMEDIAN / SKITMAKER OF THE YEAR'), ('FASHION DESIGNER OF THE YEAR', 'FASHION DESIGNER OF THE YEAR'), ('REAL ESTATE COMPANY OF THE YEAR', 'REAL ESTATE COMPANY OF THE YEAR'), ('SKINCARE BRAND OF THE YEAR', 'SKINCARE BRAND OF THE YEAR'), ('CREATIVE DIRECTOR OF THE YEAR', 'CREATIVE DIRECTOR OF THE YEAR'), ('MC OF THE YEAR', 'MC OF THE YEAR'), ('ATHLETE OF THE YEAR', 'ATHLETE OF THE YEAR'), ('SOCIAL MEDIA INFLUENCER OF THE YEAR', 'SOCIAL MEDIA INFLUENCER OF THE YEAR'), ('CONTENT CREATOR OF THE YEAR', 'CONTENT CREATOR OF THE YEAR'), ('TV STAR OF THE YEAR', 'TV STAR OF THE YEAR'), ('MAKEUP ARTISTE OF THE YEAR', 'MAKEUP ARTISTE OF THE YEAR'), ('CEO OF THE YEAR', 'CEO OF THE YEAR'), ('CREATIVE OF THE YEAR', 'CREATIVE OF THE YEAR'), ('WRITER / BLOGGER OF THE YEAR', 'WRITER / BLOGGER OF THE YEAR'), ('DJ OF THE YEAR', 'DJ OF THE YEAR')], max_length=300)),
                ('date_birth', models.DateField()),
                ('instagram_handle', models.CharField(max_length=300)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=300)),
                ('brand_name', models.CharField(max_length=300)),
                ('industry_years', models.IntegerField()),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('number_of_votes', models.IntegerField(default=0)),
                ('is_evicted', models.BooleanField(default=False)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'New Awards Registration',
                'ordering': ('-number_of_votes',),
            },
        ),
    ]
