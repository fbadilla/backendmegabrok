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
    path('reclamos/', views.ReclamosView.as_view(), name='id-reclamo-usr'),
    path('reclamos/<str:account_id>', views.ReclamosView.as_view(), name='id-reclamoid-usr'),
    path('proveedores/',views.ProveedoresView.as_view(),name='id-proveedor-usr'),
    path('proveedores/<str:id>',views.ProveedoresView.as_view(),name='id-proveedor-usr'),
    path('proveedoresAutocompletar/',views.ProveedoresAutocompletarView.as_view(),name='id-proveedor-usr'),
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
    path('generarclaim/', views.ClaimView.as_view(),name= 'id-ClaimView-usr'),
    path('GenerarClaiment/', views.GenerarClaimentIdView.as_view(),name= 'id-ClaimView-usr'),
    path('UpdatePolizas/', views.UpdatePolizasView.as_view(),name= 'id-UpdatePolizasView-usr'),
    path('UpdatePersonas/', views.UpdatePersonasView.as_view(),name= 'id-UpdatePersonasView-usr'),
    
    # SERVICIOS
    path('servicios/<str:id>', views.ServiciosView.as_view(),name= 'id-serviciosid-usr'),
    path('servicios/', views.ServiciosView.as_view(),name= 'id-serviciosid-usr'),
    #Detalles servicios
    path('detalleServicio/',views.DetallesServiciosView.as_view(),name= 'id-detallesserviciosid-usr'),
    #Documentos servicios
    path('documentos/', views.DocumentosView.as_view(), name='id-documento-usr'),
    path('documentos/<str:id>', views.DocumentosView.as_view(), name='id-documentoid-usr'),
    path('serviciosDocumentos/', views.ServiciosDocumentosView.as_view(),name= 'id-serviciosDocumentosid-usr'),
    path('serviciosDocumentos/<str:id>', views.ServiciosDocumentosView.as_view(),name= 'id-serviciosDocumentosid-usr'),
    path('serviciosproveedoresView/', views.ServiciosProveedoresView.as_view(),name= 'id-serviciosDocumentosid-usr'),
    path('serviciosproveedoresView/<str:id>', views.ServiciosProveedoresView.as_view(),name= 'id-serviciosDocumentosid-usr'),
]
