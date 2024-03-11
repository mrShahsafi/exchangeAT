
from django.contrib import admin

from exchange.models import TradingPair


@admin.register(TradingPair)
class TradingPairAdmin(admin.ModelAdmin):
    pass
