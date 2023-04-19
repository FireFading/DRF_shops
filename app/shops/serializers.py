from rest_framework import serializers
from shops.models import Shop
from streets.serializers import ShowStreetSerializer


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"


class ShowShopSerializer(serializers.ModelSerializer):
    street = ShowStreetSerializer()

    class Meta:
        model = Shop
        fields = "__all__"
