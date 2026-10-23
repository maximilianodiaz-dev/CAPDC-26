from django.db import connection
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(["GET"])
@authentication_classes([])
@permission_classes([AllowAny])
def health(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        database = cursor.fetchone() == (1,)
    return Response({"status": "ok", "database": "ok" if database else "error"})


urlpatterns = [
    path("api/health/", health),
    path("api/auth/", include("apps.iam.urls")),
    path("api/admin/", include("apps.tenant.urls")),
    path("api/negocio/", include("apps.tenant.urls_negocio")),
    path("api/catalog/", include("apps.catalog.urls")),
    path("api/leads/", include("apps.tenant.urls_leads")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
]
