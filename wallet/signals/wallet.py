from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from user.models import (
    BaseUser,
)

from wallet.models import (
    Wallet,
)

User = get_user_model()


@receiver(post_save, sender=BaseUser)
def create_user_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(user=instance)


@receiver(post_save, sender=BaseUser)
def save_user_wallet(sender, instance, **kwargs):
    try:
        instance.wallet.save()
    except User.wallet.RelatedObjectDoesNotExist:
        pass
