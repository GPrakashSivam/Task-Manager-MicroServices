from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    # Serve Swagger UI at the root path
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='root-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/',include('tasks_service.urls')),
    path('api/users/',include('users_service.urls')),
    path('api/notify/',include('notifications_service.urls')),
    
    # Swagger/OpenAPI Schema Endpoints
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Swagger UI endpoint
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # ReDoc UI endpoint
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
