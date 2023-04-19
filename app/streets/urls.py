from django.urls import path
from streets.views import StreetsListCreateView, StreetDetailView

app_name = "streets"

urlpatterns = [
    path("", StreetsListCreateView.as_view(), name="list"),
    path("<int:pk>/", StreetDetailView.as_view(), name="detail"),
]
