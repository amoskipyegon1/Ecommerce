from django.contrib import admin
from .models import (
    Category,
    SubCategory,
    Product,
    ProductVariant,
    VariantItem,
    ProductImages,
    Brand,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "categoryId"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # form = ProductAdminForm
    list_display = [
        "id",
        "name",
        "shop",
        "subCategoryId",
        "price",
        "discount",
        "inStock",
        "dateCreated",
    ]
    list_filter = ("dateCreated",)


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "productId"]


@admin.register(VariantItem)
class VariantItemAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "quantity", "variantId"]


@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ["id", "default", "productId", "variant_name"]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "categoryId"]
