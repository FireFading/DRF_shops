from rest_framework import generics
from rest_framework.response import Response
from streets.models import Street
from streets.serializers import StreetSerializer


class StreetsListCreateView(generics.ListCreateAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer

    def get(self, request, *args, **kwargs):
        queryset = Street.objects.all()
        town_id = request.query_params.get("town_id")
        if town_id is not None:
            queryset = queryset.filter(town__id=town_id)
        serializer = StreetSerializer(queryset, many=True)
        return Response(serializer.data)
