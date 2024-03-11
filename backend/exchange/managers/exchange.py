from django.db import models
from django.contrib.contenttypes.models import ContentType


class ExchangeManager(models.Manager):
    def create_buy_exchange(
            self,
            buy_exchange,
            status="P",
    ):
        buyorder_content_type = ContentType.objects.get_for_model(buy_exchange.__class__)

        instance = self.create(
            content_type=buyorder_content_type,
            content_object=buy_exchange,
            status=status
        )

        return instance
