from rest_framework import serializers

from wallet.models import Wallet

from .wallet_crrency import WalletCurrencySerializer


class WalletDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        exclude = ("user",)


class WalletDetailWithUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"


class WalletWithWalletCurrenciesSerializer(serializers.ModelSerializer):
    currency_wallet = WalletCurrencySerializer(many=True)

    class Meta:
        fields = "__all__"
