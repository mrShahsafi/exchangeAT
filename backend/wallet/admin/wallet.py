from django.contrib import admin
from wallet.models import (
    Wallet,
)

from .wallet_currency import WalletCurrencyInlineAdmin


class WalletStackedInlineAdmin(admin.StackedInline):
    model = Wallet
    extra = 1


class WalletAdmin(admin.ModelAdmin):
    model = Wallet
    raw_id_fields = ("user",)
    ordering = ("user",)
    list_display = (
        "user",
        "balance",
    )
    inlines = [
        WalletCurrencyInlineAdmin,
    ]


admin.site.register(Wallet, WalletAdmin)
