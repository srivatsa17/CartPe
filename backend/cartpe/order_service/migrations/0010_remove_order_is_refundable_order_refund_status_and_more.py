# Generated by Django 4.2 on 2024-03-02 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_service', '0009_rename_pending_amount_order_amount_due_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='is_refundable',
        ),
        migrations.AddField(
            model_name='order',
            name='refund_status',
            field=models.CharField(choices=[('NA', 'NA'), ('INITIATED', 'INITIATED'), ('PARTIAL', 'PARTIAL'), ('COMPLETED', 'COMPLETED'), ('FAILED', 'FAILED')], default='NA', max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PENDING', 'PENDING'), ('CONFIRMED', 'CONFIRMED'), ('SHIPPED', 'SHIPPED'), ('OUT_FOR_DELIVERY', 'OUT_FOR_DELIVERY'), ('DELIVERED', 'DELIVERED'), ('CANCELLED', 'CANCELLED'), ('RETURNED', 'RETURNED')], default='PENDING', max_length=255),
        ),
    ]