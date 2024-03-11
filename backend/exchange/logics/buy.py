from django.contrib.auth import get_user_model
from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework import (
    status,
)

from core.responses import (
    UNKNOWN_EN
)

from backend.settings import MIN_ORDER_PRICE_AGGREGATOR

from asset.models import Currency

from exchange.models import BuyOrder,Exchange,TradingPair
from exchange.utils import buy_from_exchange

from wallet.models import (
    WalletCurrency
)

User = get_user_model()


@transaction.atomic
def buy_order_logic(serializer: serializers, user: User):
    order_amount = serializer.data["amount"]
    user_wallet = user.wallet
    currency = get_object_or_404(Currency, name=serializer.data["name"])
    price = order_amount * currency.price
    try:
        user_wallet.debit(price)
        wallet_currency,created = WalletCurrency.objects.get_or_create(
            wallet=user_wallet, currency=currency
        )
        trading_pair,created = TradingPair.objects.get_or_create(
            base_currency = None,
            quote_currency = currency
        )
        buy_order = BuyOrder.objects.select_for_update().create(
            user=user, amount=order_amount, price=currency.price,
            trade_pair=trading_pair
        )
        if price > MIN_ORDER_PRICE_AGGREGATOR:
            # do the exchange logic
            success_buy = buy_from_exchange(currency.name, order_amount)
            if not success_buy:
                return None, status.HTTP_500_INTERNAL_SERVER_ERROR, UNKNOWN_EN
            wallet_currency.credit(order_amount)
            Exchange.objects.create_buy_exchange(
                buy_exchange=buy_order,
                status="A"
            )
            buy_order.status = "A"
            buy_order.save()
        return buy_order, status.HTTP_201_CREATED, None
    except Exception as e:
        return None, status.HTTP_400_BAD_REQUEST, e