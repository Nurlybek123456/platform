from django.urls import path

from . import views

app_name = 'users'


urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('register', views.register_view, name='register'),
    path('login', views.login_view, name='login'),
    path('refresh', views.refresh_token_view, name='token_refresh'),
]
