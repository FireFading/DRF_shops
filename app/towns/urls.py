from django.urls import path
from towns.views import TownDetailView, TownsListCreateView

app_name = "towns"

urlpatterns = [
    path("", TownsListCreateView.as_view(), name="list"),
    path("<int:pk>/", TownDetailView.as_view(), name="detail"),
]
