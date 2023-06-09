# Generated by Django 3.2.9 on 2022-11-07 22:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20221015_2229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, choices=[('ar', 'Arabic'), ('en', 'English')], max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(blank=True, max_length=255, null=True)),
                ('birth_date', models.DateField()),
                ('country', models.CharField(blank=True, choices=[('Alex', 'Alex'), ('Cairo', 'Cairo')], max_length=20, null=True)),
                ('company', models.CharField(blank=True, max_length=50, null=True)),
                ('company_url', models.URLField(blank=True, null=True)),
                ('twitter_url', models.URLField(blank=True, null=True)),
                ('facebook_url', models.URLField(blank=True, null=True)),
                ('linkedin_url', models.URLField(blank=True, null=True)),
                ('instagram_url', models.URLField(blank=True, null=True)),
                ('quora_url', models.URLField(blank=True, null=True)),
                ('image', models.ManyToManyField(blank=True, to='user.Languages')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
