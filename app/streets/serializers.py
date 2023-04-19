from rest_framework import serializers
from streets.models import Street
from towns.serializers import TownSerializer


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = "__all__"


class ShowStreetSerializer(serializers.ModelSerializer):
    town = TownSerializer()

    class Meta:
        model = Street
        fields = "__all__"
