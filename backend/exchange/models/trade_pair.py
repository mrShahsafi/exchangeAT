from django.db import models


class TradingPair(models.Model):
    base_currency = models.ForeignKey(
        "asset.Currency", on_delete=models.CASCADE, related_name="base_pairs",
        null=True,blank=True
    )
    quote_currency = models.ForeignKey(
        "asset.Currency", on_delete=models.CASCADE, related_name="quote_pairs",
        null=True, blank=True
    )
    #
    # def __str__(self):
    #     return f"{self.base_currency.symbol}-{self.quote_currency.symbol}"
