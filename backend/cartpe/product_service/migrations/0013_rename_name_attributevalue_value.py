# Generated by Django 4.2 on 2023-05-12 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_service', '0012_rename_attribute_product_attributes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attributevalue',
            old_name='name',
            new_name='value',
        ),
    ]
