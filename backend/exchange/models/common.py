from django.db import models
from django.contrib.auth import get_user_model

from core.models import CommonBaseModel

User = get_user_model()


class CommonOrder(CommonBaseModel):
    class Meta:
        abstract = True

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    price = models.FloatField(default=0)
    trade_pair = models.ForeignKey(
        "exchange.TradingPair", on_delete=models.CASCADE,null=True,blank=True
    )
