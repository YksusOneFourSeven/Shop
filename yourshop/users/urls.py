from django.contrib.auth.views import LogoutView, LoginView, PasswordChangeView
from django.urls import path
from . import views
from .views import AccountView
from django.contrib.auth.decorators import login_required

app_name = 'users'

urlpatterns = [
    path('account/', AccountView.as_view(), name='account'),
    path(
        'logout/',
        LogoutView.as_view(next_page='store:home'),
        name='logout',),
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login',),
    path(
        'passwordChange/',
        PasswordChangeView.as_view(template_name='users/password_change.html'),
        name='passwordChange',),
    path(
        'signup/', views.SignUp.as_view(), name='signup'),

]
