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
    path('reclamos/', views.ReclamoView.as_view(), name='id-reclamo-usr'),
    path('reclamos/<str:account_id>', views.ReclamoView.as_view(), name='id-reclamoid-usr'),
    path('documentos/', views.DocumentoView.as_view(), name='id-documento-usr'),
    path('documentos/<str:reclamo_id>', views.DocumentoView.as_view(), name='id-documentoid-usr'),
    path('proveedores/',views.ProveedorView.as_view(),name='id-proveedor-usr'),
    path('formulario/<str:reclamo_id>',views.FormularioView.as_view(),name='id-formulario-usr'),
    path('planes/', views.PlanesView.as_view(), name='id-planes-usr'),
    path('planes/<str:plan_id>', views.PlanesView.as_view(), name='id-planesid-usr'),
    path('polizas/', views.PolizasView.as_view(), name='id-polizas-usr'),
    path('polizas/<str:Poliza_id>', views.PolizasView.as_view(), name='id-polizasid-usr'),
    path('agentes/', views.AgentesVentasView.as_view(), name='id-agentes-usr'),
    path('agentes/<str:agente_id>', views.AgentesVentasView.as_view(), name='id-agentesid-usr'),
    path('personas/', views.PersonasView.as_view(), name='id-personas-usr'),
    path('personas/<str:persona_id>', views.PersonasView.as_view(), name='id-personasid-usr'),
    path('asociacion/', views.AsociacionPolizasView.as_view(), name='id-asociacion-usr'),
    path('asociacion/<str:asociacion_id>', views.AsociacionPolizasView.as_view(), name='id-asociacionid-usr'),
]
