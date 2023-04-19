from rest_framework import serializers
from towns.models import Town


class TownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Town
        fields = "__all__"
