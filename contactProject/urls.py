
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Mini Django Project",
        default_version='v1',
        description="",
        terms_of_service="https://www.myapp.com/policies/terms/",
        contact=openapi.Contact(email="contact@digitalberry.local"),
        license=openapi.License(name="Contact License"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('contact/', include('contact.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
