from django.contrib import admin

from exchange.models import Exchange


@admin.register(Exchange)
class ExchangeAdmin(admin.ModelAdmin):
    pass
