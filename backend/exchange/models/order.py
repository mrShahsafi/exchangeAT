from django.db import models
from django.contrib.auth import get_user_model

from exchange.managers import BuyOrderManager

from .common import CommonOrder

User = get_user_model()

ORDER_STATUS = [
    ("P", "Pending"),
    ("A", "Accepted"),
    ("R", "Rejected"),
    ("C", "Canceled"),
]


class BuyOrder(CommonOrder):
    status = models.CharField(max_length=1, choices=ORDER_STATUS, default="P")
    objects = BuyOrderManager()


class SellOrder(CommonOrder):
    status = models.CharField(max_length=1, choices=ORDER_STATUS, default="P")
