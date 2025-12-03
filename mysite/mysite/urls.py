from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path
from django.contrib import admin


schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Django REST API Swagger documentation",
    ),
    public=True,
)



urlpatterns = [
    path('admin/', admin.site.urls),

    # Swagger UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),

    # ReDoc
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-ui'),
]


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('udemy_app.urls')),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.urls import include, path
urlpatterns = [
    path('api/', include('movies.urls')),
    path('api/auth/', include('rest_framework.urls')),
    # allauth / jwt routes сен койгонуң боюнча
]
