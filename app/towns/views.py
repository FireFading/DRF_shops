from rest_framework import generics
from towns.models import Town
from towns.serializers import TownSerializer


class TownsListCreateView(generics.ListCreateAPIView):
    queryset = Town.objects.all()
    serializer_class = TownSerializer
