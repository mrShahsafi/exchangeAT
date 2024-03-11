from random import randint

from django.db import models

from core.models import CommonBaseModel


class Currency(CommonBaseModel):
    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"

    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name
    #
    # @property
    # def price(self):
    #     return randint(10, 31)
