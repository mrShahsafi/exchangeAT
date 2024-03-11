from django.urls import path, include

from .views import BuyOrderApi

urlpatterns = [
    path("buy/", BuyOrderApi.as_view(), name="buy_order"),
    ]
