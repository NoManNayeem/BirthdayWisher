from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions


from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Set the Django admin header
admin.site.site_header = 'Birthday-Wisher'

# Configure API documentation view
schema_view = get_schema_view(
    openapi.Info(
        title="Birthday-Wisher API",
        default_version='v1',
        description="API documentation for Birthday-Wisher",
        terms_of_service="https://Birthday-Wisher.com/",
        contact=openapi.Contact(email="your_email@Birthday-Wisher.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # API Documentation
    path('api-docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),



    # Include project-apps' URLs here
    path('', include('customers.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)