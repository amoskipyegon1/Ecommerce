from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "backend.products"
    label = "products"
    verbose_name = "Shop Products"
