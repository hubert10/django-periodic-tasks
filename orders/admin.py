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
    list_display = ("currency_name", "currency_label", "id")
    search_fields = [
        "currency_name",
    ]
    list_per_page = 50


@admin.register(CurrencyRate)
class CurrencyRateAdmin(admin.ModelAdmin):
    list_display = ("currency_rate", "currency_label", "id")
    search_fields = [
        "currency_rate",
    ]
    list_per_page = 50
