from django.db import models
from django.contrib.auth import get_user_model

from .common import CommonBaseWallet

User = get_user_model()


class Wallet(CommonBaseWallet):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    currency = models.CharField(
        max_length=3, default="USD"
    )  # TODO: add support for other currencies

    def __str__(self):
        return f"{self.user.email}'s Wallet"
