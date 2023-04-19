from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("towns/", include("towns.urls")),
    path("streets/", include("streets.urls")),
    path("shops/", include("shops.urls")),
]
