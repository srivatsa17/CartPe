# Generated by Django 4.2 on 2023-05-11 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_service', '0007_attribute_attributevalue_product_attribute_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='attribute_value',
            field=models.ManyToManyField(blank=True, related_name='products', to='product_service.attributevalue'),
        ),
    ]