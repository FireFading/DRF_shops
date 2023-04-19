from datetime import datetime

from django.db.models import Q
from rest_framework import generics, status
from rest_framework.response import Response
from shops.models import Shop
from shops.serializers import ShopSerializer, ShowShopSerializer
from streets.models import Street


class ShopsListCreateView(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def post(self, request, *args, **kwargs):
        if not Street.objects.filter(id=request.data["street"]).exists():
            return Response(
                data={"error": "This street does not exist."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Shop.objects.all()
        street_id = self.request.query_params.get("street_id")
        town_id = self.request.query_params.get("town_id")
        name = self.request.query_params.get("name")
        shop_open = self.request.query_params.get("open")
        if street_id is not None:
            queryset = queryset.filter(street__id=street_id)
        if town_id is not None:
            queryset = queryset.filter(street__town__id=town_id)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        if shop_open is not None:
            current_time = datetime.now().time()
            if shop_open == "1":
                queryset = queryset.filter(Q(opening_time__lte=current_time) & Q(closing_time__gt=current_time))
            else:
                queryset = queryset.filter(
                    Q(closing_time__lte=current_time)
                    | Q(
                        opening_time__gt=current_time,
                    )
                )
        return queryset


class ShopDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShowShopSerializer
