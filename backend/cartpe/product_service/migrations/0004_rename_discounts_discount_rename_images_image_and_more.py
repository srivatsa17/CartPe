# Generated by Django 4.2 on 2023-04-25 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_service', '0003_images'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Discounts',
            new_name='Discount',
        ),
        migrations.RenameModel(
            old_name='Images',
            new_name='Image',
        ),
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]