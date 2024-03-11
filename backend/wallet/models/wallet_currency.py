from django.db import models

from .common import CommonBaseWallet


class WalletCurrency(CommonBaseWallet):
    class Meta:
        verbose_name = "Currency Wallet"
        verbose_name_plural = "Currency Wallets"
        unique_together = [
            ("wallet", "currency"),
        ]

    wallet = models.ForeignKey(
        "wallet.Wallet", on_delete=models.CASCADE, related_name="currency_wallet"
    )
    currency = models.ForeignKey(
        "asset.Currency",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.wallet}, {self.currency},"
