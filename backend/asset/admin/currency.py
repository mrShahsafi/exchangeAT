from django.contrib import admin
from asset.models import (
    Currency,
)


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    model = Currency
    ordering = ("name",)
    list_display = (
        "name",
        "symbol",
        "price",
    )
