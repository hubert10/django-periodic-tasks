from django.contrib import admin
from .models import Order, Product, Currency, CurrencyRate


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "added")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "description")


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "label",
    )
    search_fields = [
        "name",
    ]
    list_per_page = 50


@admin.register(CurrencyRate)
class CurrencyRateAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "rate",
        "label",
    )
    search_fields = [
        "rate",
    ]
    list_per_page = 50
