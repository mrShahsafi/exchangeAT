from rest_framework import serializers

from exchange.models import BuyOrder


class BuyOrderInptSerializer(serializers.Serializer):
    name = serializers.CharField()
    amount = serializers.FloatField()


class BuyOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyOrder
        fields = '__all__'

