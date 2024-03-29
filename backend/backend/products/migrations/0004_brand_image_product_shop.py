# Generated by Django 4.2 on 2023-04-24 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_sellerdetails"),
        ("products", "0003_alter_product_options_product_quantity"),
    ]

    operations = [
        migrations.AddField(
            model_name="brand",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AddField(
            model_name="product",
            name="shop",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="shop_product",
                to="users.seller",
            ),
        ),
    ]
