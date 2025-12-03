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


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('udemy_app.urls')),
    path('accounts/', include('allauth.urls')),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.urls import include, path
urlpatterns = [
    path('api/', include('movies.urls')),
    path('api/auth/', include('rest_framework.urls')),
    # allauth / jwt routes сен койгонуң боюнча
]
