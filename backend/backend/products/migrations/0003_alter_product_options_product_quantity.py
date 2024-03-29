# Generated by Django 4.2 on 2023-04-18 17:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_product_searchtags_brand_product_brand"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name": "Product", "verbose_name_plural": "Products"},
        ),
        migrations.AddField(
            model_name="product",
            name="quantity",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
