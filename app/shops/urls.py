from django.urls import path
from shops.views import ShopDetailView, ShopsListCreateView

app_name = "shops"

urlpatterns = [
    path("", ShopsListCreateView.as_view(), name="list"),
    path("<int:pk>/", ShopDetailView.as_view(), name="detail"),
]
