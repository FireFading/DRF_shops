from django.urls import path
from towns.views import TownsListCreateView

app_name = "towns"

urlpatterns = [
    path("", TownsListCreateView.as_view(), name="list"),
]
