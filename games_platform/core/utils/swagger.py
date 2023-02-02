from django.urls import include, path, re_path
from django.views.generic import TemplateView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Graduaders Backend API",
        default_version='0.0.1',
        description="'Graduaders' team HTML5 games platform backend API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="180107180@stu.sdu.edu.kz"),
        license=openapi.License(name="MIT License"),
    ),
    patterns=[path('api/', include('core.urls')), ],
    public=True,
    permission_classes=(permissions.AllowAny,),
)

swagger_urls = [
    re_path(
        route='swagger-ui/',
        view=TemplateView.as_view(
            template_name='swagger/swagger.html',
            extra_context={'schema_url': 'openapi-schema'}
        ),
        name='swagger-ui'),
    re_path(
        route=r'^swagger(?P<format>\.json|\.yaml)$',
        view=schema_view.without_ui(cache_timeout=0),
        name='schema-json'),
]