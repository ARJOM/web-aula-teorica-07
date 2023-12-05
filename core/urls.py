from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Login
    # https://docs.djangoproject.com/en/2.0/topics/auth/default/#django.contrib.auth.views.LoginView
    path('login/', views.CustomLoginView.as_view(), name='login'),

    # Logout
    # https://docs.djangoproject.com/en/2.0/topics/auth/default/#django.contrib.auth.views.LogoutView
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', views.TelaProtegida.as_view(), name='home'),
    path('signup/', views.NovoUsuario.as_view(), name='signup')
]