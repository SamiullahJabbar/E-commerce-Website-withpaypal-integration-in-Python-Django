# Generated by Django 5.0.6 on 2024-06-26 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='total_amount',
        ),
    ]