# Generated by Django 4.2 on 2023-04-28 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_service', '0007_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
