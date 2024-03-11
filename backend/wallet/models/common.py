from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from core.models import CommonBaseModel

User = get_user_model()


class CommonBaseWallet(CommonBaseModel):
    class Meta:
        abstract = True

    balance = models.FloatField(default=0)
    is_blocked = models.BooleanField(default=False)

    def credit(self, amount, commit=True):
        self.validate_credit(amount)
        self.balance += amount
        if commit:
            self.save()

    def debit(self, amount, commit=True):
        self.validate_debit(amount)
        self.balance -= amount
        if commit:
            self.save()
        return True

    def validate_credit(self, amount):
        """
        Validate whether the wallet is not blocked.
        """
        self.validate_block()
        return True

    def validate_debit(self, amount):
        """
        Validate whether the wallet has sufficient balance for the debit operation.
        """
        self.validate_block()
        if self.balance < amount:
            raise ValidationError("Wallet is not sufficient.")
        return True

    def validate_block(self):
        if self.is_blocked:
            raise ValidationError("Wallet is blocked.")
        return True

    def block(self, commit=True):
        self.is_blocked = True
        if commit:
            self.save()
