# Generated by Django 4.1 on 2022-11-14 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_auto_20221015_2330'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('Black', 'Black'), ('White', 'White'), ('Red', 'Red'), ('Blue', 'Blue'), ('Green', 'Green')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SizeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='color1',
        ),
        migrations.RemoveField(
            model_name='product',
            name='color2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='color3',
        ),
        migrations.RemoveField(
            model_name='product',
            name='color4',
        ),
        migrations.RemoveField(
            model_name='product',
            name='color5',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size1',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size3',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size4',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size5',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size6',
        ),
        migrations.AddField(
            model_name='product',
            name='colors',
            field=models.ManyToManyField(blank=True, to='product.colormodel'),
        ),
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.ManyToManyField(blank=True, to='product.sizemodel'),
        ),
    ]
