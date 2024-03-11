from django.db.models import F, Sum,Manager


class BuyOrderManager(Manager):
    def group_by_pending(
        self,
    ):
        qs = (
            self.filter(status='P')
                .annotate(currency_name=F('trade_pair__quote_currency__name'))
                .values("currency_name")
                .annotate(total_pending_amount=Sum('amount'))
        )
        return qs
