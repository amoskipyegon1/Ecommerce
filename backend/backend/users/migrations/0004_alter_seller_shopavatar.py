# Generated by Django 4.2 on 2023-04-17 18:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_alter_appuser_options_alter_seller_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="seller",
            name="shopAvatar",
            field=models.ImageField(upload_to=""),
        ),
    ]
