from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from users import urls as users_urls
from .utils.swagger import swagger_urls

urlpatterns = [
    path('admin/', admin.site.urls, name="admin-panel"),
    path('users/', include(users_urls)),
    path(route="", view=include(arg="games.urls")),
] + swagger_urls
