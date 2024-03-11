from django.db import models


class CommonBaseQuerySet(models.QuerySet):
    def business_layer(self):
        return self.model.objects.filter(
            is_active=True,
            is_deleted=False,
        )


class AllActiveManager(models.Manager):
    def get_queryset(self):
        return CommonBaseQuerySet(self.model, using=self._db)

    def business_layer(self):
        return self.get_queryset().business_layer()


class CommonBaseManager(models.Manager):
    def all_active(
        self,
    ):

        queryset = self.filter(
            is_active=True,
            is_deleted=False,
        )

        return queryset
