# Generated by Django 3.2.9 on 2022-11-07 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_languages_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='image',
            new_name='langs',
        ),
    ]