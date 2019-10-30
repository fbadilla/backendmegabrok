from django.contrib import admin
from django.urls import path, include
from api import views, viewToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
urlpatterns = [
    path('token/', viewToken.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('registro/', views.Registro.as_view(), name='id-registro'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('account/', views.AccountView.as_view(), name='id-Account-usr'),
    path('profile/', views.ProfileView.as_view(), name='id-profile-usr'),
    path('roles/', views.RolView.as_view(), name='id-grupo-usr'),
    path('eventos/', views.EventoView.as_view(), name='id-evento-usr'),
    path('documentos/', views.ServicioView.as_view(), name='id-servicio-usr'),
    path('reclamos/', views.ReclamoView.as_view(), name='id-reclamo-usr'),
]
