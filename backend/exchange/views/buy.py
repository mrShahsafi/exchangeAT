from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import (
    status,
)
from rest_framework.permissions import (
    IsAuthenticated,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from exchange.logics import buy_order_logic
# Local response
from exchange.serializers import (
    BuyOrderSerializer,BuyOrderInptSerializer
)

# from user.tasks import (
#     send_forgot_password_link,
# )

User = get_user_model()


class BuyOrderApi(
    APIView,
):
    permission_classes = (IsAuthenticated,)
    serializer_class = BuyOrderInptSerializer

    @transaction.atomic
    def post(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        buy_order, status_code, error = buy_order_logic(
            serializer, user
        )
        if error:
            return Response(
                {"error": str(error)},
                status=status_code
            )
        return Response(
            BuyOrderSerializer(buy_order).data,
            status=status.HTTP_201_CREATED
        )
