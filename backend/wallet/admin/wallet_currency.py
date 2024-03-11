from django.contrib import admin

from wallet.models import WalletCurrency


class WalletCurrencyInlineAdmin(admin.StackedInline):
    model = WalletCurrency
    extra = 0


class WalletCurrencyAdmin(admin.ModelAdmin):
    model = WalletCurrency


admin.site.register(WalletCurrency, WalletCurrencyAdmin)
