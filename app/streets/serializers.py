from rest_framework import serializers
from streets.models import Street


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = "__all__"
