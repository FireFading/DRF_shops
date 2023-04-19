from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

info = openapi.Info(
    title="Django Shops API",
    default_version="v1",
    description="",
    contact=openapi.Contact(email="firefading@mail.ru"),
)

schema_view = get_schema_view(
    info,
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("towns/", include("towns.urls")),
    path("streets/", include("streets.urls")),
    path("shops/", include("shops.urls")),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]
