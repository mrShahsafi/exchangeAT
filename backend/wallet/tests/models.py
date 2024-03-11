from django.test import TestCase
from wallet.models import Wallet
from user.models import BaseUser


class WalletModelTestCase(TestCase):
    def setUp(self):
        user = BaseUser.objects.create_superuser(
            email="test@example.com",
            password="VerryStrongPass123098754321213",
        )
        self.wallet = user.wallet

    def test_debit_to_wallet(self):
        initial_balance = self.wallet.balance
        amount = 500  # Debit amount

        # Debit the wallet
        debit = self.wallet.debit(amount)

        # Check if the transaction was properly created
        self.assertIsNotNone(debit)
        self.assertEqual(self.wallet.amount, amount)

    def test_insufficient_balance(self):
        # Attempt to debit an amount greater than the current balance
        amount = 1500
        user = BaseUser.objects.create(email="insufficient@example.com",)
        self.assertRaises(ValueError, user.wallet.debit, amount)

# Add more test cases as needed
