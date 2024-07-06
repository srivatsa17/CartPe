# Generated by Django 4.2.11 on 2024-06-03 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='topic',
            field=models.CharField(choices=[('Order Status', 'Order Status'), ('Shipping and Delivery', 'Shipping and Delivery'), ('Returns and Refunds', 'Returns and Refunds'), ('Payment Issues', 'Payment Issues'), ('Account Issues', 'Account Issues'), ('Product Inquiry', 'Product Inquiry'), ('Technical Support', 'Technical Support'), ('Feedback and Suggestions', 'Feedback and Suggestions'), ('Report a Problem', 'Report a Problem'), ('General Inquiry', 'General Inquiry')], default='Order Status', max_length=255),
        ),
    ]