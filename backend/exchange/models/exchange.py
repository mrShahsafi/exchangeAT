from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


from core.models import CommonBaseModel

from exchange.managers import ExchangeManager


POSITION_CHOICES = models.Q(app_label="exchange", model="buyorder") | models.Q(
    app_label="exchange", model="sellorder"
)

EXCHANGE_STATUS = [
    ("P", "Pending"),
    ("A", "Accepted"),
    ("R", "Rejected"),
    ("C", "Canceled"),
]


class Exchange(CommonBaseModel):

    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE,
        limit_choices_to=POSITION_CHOICES
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    status = models.CharField(max_length=1, choices=EXCHANGE_STATUS, default="P")

    objects = ExchangeManager()