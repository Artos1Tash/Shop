# Generated by Django 4.1.1 on 2022-09-22 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0004_remove_cart_cart_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart_product',
            name='cart_id',
        ),
        migrations.RemoveField(
            model_name='cart_product',
            name='product_id',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Cart_product',
        ),
    ]
