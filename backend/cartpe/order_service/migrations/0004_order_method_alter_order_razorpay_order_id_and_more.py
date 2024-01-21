# Generated by Django 4.2 on 2024-01-15 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_service', '0003_alter_order_razorpay_order_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='method',
            field=models.CharField(choices=[('UPI', 'UPI'), ('CASH_ON_DELIVERY', 'CASH_ON_DELIVERY')], default='UPI', max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='razorpay_order_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='razorpay_payment_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='razorpay_signature',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PENDING', 'PENDING'), ('CONFIRMED', 'CONFIRMED'), ('SHIPPED', 'SHIPPED'), ('OUT_FOR_DELIVERY', 'OUT_FOR_DELIVERY'), ('DELIVERED', 'DELIVERED'), ('CANCELLED', 'CANCELLED'), ('RETURNED', 'RETURNED')], default='PENDING', max_length=255),
        ),
    ]