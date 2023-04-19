from django.urls import path
from streets.views import StreetsListCreateView

app_name = "streets"

urlpatterns = [
    path("", StreetsListCreateView.as_view(), name="list"),
]
