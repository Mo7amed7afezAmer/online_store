# Generated by Django 4.1 on 2022-12-14 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_auto_20221015_2234'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='checkout',
            options={'verbose_name': 'CheckOut', 'verbose_name_plural': 'CheckOuts'},
        ),
        migrations.AlterModelOptions(
            name='nonuserorder',
            options={'verbose_name': 'NonUser Order', 'verbose_name_plural': 'NonUser Orders'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
    ]