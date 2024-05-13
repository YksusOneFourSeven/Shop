# users/urls.py

# Импортируем из приложения django.contrib.auth нужный view-класс
from django.contrib.auth.views import LogoutView, LoginView, PasswordChangeView
from django.urls import path

app_name = 'users'

urlpatterns = [
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout',
    ),
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login',
    ),
    path(
        'passwordChange/',
        PasswordChangeView.as_view(template_name='users/password_change.html'),
        name='passwordChange',
    ),
]