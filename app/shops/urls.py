from django.urls import path
from shops.views import ShopsListCreateView

app_name = "shops"

urlpatterns = [
    path("", ShopsListCreateView.as_view(), name="list"),
]
