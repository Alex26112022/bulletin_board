from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from config import settings
from users.views import CustomUserViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Board API",
        default_version='v1',
        description="Board description",
        terms_of_service="http://89.169.167.48",
        contact=openapi.Contact(email="AlexeyDenisenko2703@yandex.ru"),
        license=openapi.License(name="Alex License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register("users", CustomUserViewSet)

urlpatterns = [
                  path('', include('djoser.urls.jwt')),
                  path('swagger<format>/',
                       schema_view.without_ui(cache_timeout=0),
                       name='schema-json'),
                  path('swagger/',
                       schema_view.with_ui('swagger', cache_timeout=0),
                       name='schema-swagger-ui'),
                  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
                       name='schema-redoc'),
                  path('admin/', admin.site.urls),
                  path('api/',
                       include('bulletins.urls', namespace='bulletins'))
              ] + router.urls

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
