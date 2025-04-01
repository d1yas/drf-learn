from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi




# schema_view = get_schema_view(
#    openapi.Info(
#       title="Snippets API",
#       default_version='v1',
#       description="Test description",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@snippets.local"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )



urlpatterns = [
                    path('admin/', admin.site.urls),
                    path('user/', include('UserApp.urls')),
                    path('api/drf-auth/', include('rest_framework.urls')),
                    path('api/dj-rest-auth/', include('dj_rest_auth.urls')),
                    path('api/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
                    # spectacular
                    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
                    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
                    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
                    
                    # drf-yasg
                    # path('swagger.<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
                    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


              ] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])


# urlpatterns = [
#     # YOUR PATTERNS
#     path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
#     # Optional UI:
#     path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
#     path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
# ]