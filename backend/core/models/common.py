from django.db import models

from core.managers import CommonBaseManager, AllActiveManager


class CommonBaseModel(models.Model):
    """
    this is an abstract model
    We inherit this table for most of our tables to add latest created and updated in table
    is_deleted is a property when we dont want to actually delete something and we just
        dont want to show it to the user
    """

    created_date = models.DateTimeField(
        auto_now_add=True,
    )
    updated_date = models.DateTimeField(
        auto_now=True,
    )
    is_deleted = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=True,
    )
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    objects = CommonBaseManager()
    all_active = AllActiveManager()

    class Meta:
        abstract = True

    def safe_delete(
        self,
        commit=True,
    ):
        self.is_active = False
        self.is_deleted = True
        if commit:
            self.save()

    def save(self, *args, **kwargs):
        if self.is_deleted:
            self.is_active = False
        super().save(*args, **kwargs)
