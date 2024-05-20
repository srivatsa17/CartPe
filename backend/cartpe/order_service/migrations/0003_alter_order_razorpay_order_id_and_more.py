# Generated by Django 4.2 on 2023-11-14 11:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order_service', '0002_rename_total_price_order_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='razorpay_order_id',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='razorpay_payment_id',
            field=models.CharField(default='order', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='razorpay_signature',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Order Pending'), ('CONFIRMED', 'Order Confirmed'), ('SHIPPED', 'Shipped'), ('OUT_FOR_DELIVERY', 'Out for Delivery'), ('DELIVERED', 'Delivered'), ('CANCELLED', 'Cancelled'), ('RETURNED', 'Returned')], default='PENDING', max_length=255),
        ),
    ]
