from rest_framework import serializers

from wallet.models import WalletCurrency


class WalletCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletCurrency
        exclude = ("wallet",)
