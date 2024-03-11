from django.db import transaction
from django.contrib.auth import get_user_model

from celery import (
    shared_task,
)


from exchange.models import BuyOrder
from exchange.utils import buy_from_exchange
from exchange.models import Exchange

User = get_user_model()


@shared_task
@transaction.atomic
def complete_order_task(order_id):
    try:
        buy_order = BuyOrder.objects.select_related(
            'trade_pair__quote_currency'
        ).get(id=order_id)
        currency = buy_order.trade_pair.quote_currency
        wallet_currency = currency.walletcurrency_set.get(
            wallet=buy_order.user.wallet,
            currency=currency
        )
        wallet_currency.credit(buy_order.amount)
        buy_order.status = "A"
        buy_order.save()
        Exchange.objects.create_buy_exchange(
            buy_exchange=buy_order,
            status="A"
        )
    except Exception:
        pass


@shared_task
def perform_bulk_exchange_request_task(name, amount, id_list):
    try:
        success_status = buy_from_exchange(name, amount)
        if success_status:
            for order_id in id_list:
                complete_order_task.delay(order_id)
        # else:
            # set status to R and fill user's wallet
    except Exception:
        pass


@shared_task
def get_pending_buy_orders_task():
    """
        PERIODIC TASK
    """
    try:
        grouped_orders = BuyOrder.objects.group_by_pending()
        buy_orders_ids = [i[0] for i in grouped_orders.values_list('id')]
        for group in grouped_orders:
            perform_bulk_exchange_request_task.delay(
                group['currency_name'],
                group['total_pending_amount'],
                buy_orders_ids
            )
    except Exception as error:
        print(error)
