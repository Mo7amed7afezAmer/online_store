# Generated by Django 4.1 on 2022-11-25 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_colormodel_sizemodel_remove_product_color1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_products', models.PositiveIntegerField(default=0)),
                ('price100', models.PositiveIntegerField(default=0)),
                ('price200', models.PositiveIntegerField(default=0)),
                ('price300', models.PositiveIntegerField(default=0)),
                ('price400', models.PositiveIntegerField(default=0)),
                ('price500', models.PositiveIntegerField(default=0)),
                ('black', models.PositiveIntegerField(default=0)),
                ('white', models.PositiveIntegerField(default=0)),
                ('red', models.PositiveIntegerField(default=0)),
                ('blue', models.PositiveIntegerField(default=0)),
                ('green', models.PositiveIntegerField(default=0)),
                ('xs', models.PositiveIntegerField(default=0)),
                ('s', models.PositiveIntegerField(default=0)),
                ('m', models.PositiveIntegerField(default=0)),
                ('l', models.PositiveIntegerField(default=0)),
                ('xl', models.PositiveIntegerField(default=0)),
                ('xxl', models.PositiveIntegerField(default=0)),
                ('male', models.PositiveIntegerField(default=0)),
                ('female', models.PositiveIntegerField(default=0)),
                ('baby', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='colormodel',
            name='color',
            field=models.CharField(choices=[('Black', 'Black'), ('White', 'White'), ('Red', 'Red'), ('Blue', 'Blue'), ('Green', 'Green'), ('Yellow', 'Yellow'), ('Orange', 'Orange'), ('Brown', 'Brown'), ('Pink', 'Pink'), ('Rose', 'Rose')], max_length=20),
        ),
    ]
