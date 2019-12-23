from django.contrib import admin
from django.urls import path, include
from api import  viewToken
from .views import personas,polizas,proveedores,reclamos,usuarios
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
urlpatterns = [
    path('token/', viewToken.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    path('registro/', usuarios.Registro.as_view(), name='id-registro'),
    path('account/', usuarios.AccountView.as_view(), name='id-Account-usr'),
    path('profile/', usuarios.ProfileView.as_view(), name='id-profile-usr'),
    path('roles/', usuarios.RolView.as_view(), name='id-grupo-usr'),
    path('agentes/', usuarios.AgentesVentasView.as_view(), name='id-agentes-usr'),
    path('agentes/<str:agente_id>', usuarios.AgentesVentasView.as_view(), name='id-agentesid-usr'),
    
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('proveedores/',proveedores.ProveedoresView.as_view(),name='id-proveedor-usr'),
    path('proveedores/<str:id>',proveedores.ProveedoresView.as_view(),name='id-proveedor-usr'),
    path('proveedoresAutocompletar/',proveedores.ProveedoresAutocompletarView.as_view(),name='id-proveedor-usr'),
    path('formulario/<str:reclamo_id>',reclamos.FormularioView.as_view(),name='id-formulario-usr'),
    path('planes/', polizas.PlanesView.as_view(), name='id-planes-usr'),
    path('planes/<str:plan_id>', polizas.PlanesView.as_view(), name='id-planesid-usr'),
    path('polizas/', polizas.PolizasView.as_view(), name='id-polizas-usr'),
    path('polizas/<str:Poliza_id>', polizas.PolizasView.as_view(), name='id-polizasid-usr'),
    path('personas/', personas.PersonasView.as_view(), name='id-personas-usr'),
    path('personas/<str:persona_id>', personas.PersonasView.as_view(), name='id-personasid-usr'),
    path('asociacion/', polizas.AsociacionPolizasView.as_view(), name='id-asociacion-usr'),
    path('asociacion/<str:asociacion_id>', polizas.AsociacionPolizasView.as_view(), name='id-asociacionid-usr'),
    path('GenerarClaiment/', reclamos.GenerarClaimentIdView.as_view(),name= 'id-ClaimView-usr'),
    path('UpdatePolizas/', polizas.UpdatePolizasView.as_view(),name= 'id-UpdatePolizasView-usr'),
    path('UpdatePersonas/', personas.UpdatePersonasView.as_view(),name= 'id-UpdatePersonasView-usr'),
    
    
    path('reclamos/', reclamos.ReclamosView.as_view(), name='id-reclamo-usr'),
    path('reclamos/<str:account_id>', reclamos.ReclamosView.as_view(), name='id-reclamoid-usr'),
    path('generarclaim/', reclamos.ClaimView.as_view(),name= 'id-ClaimView-usr'),
    # SERVICIOS
    path('servicios/<str:id>', reclamos.ServiciosView.as_view(),name= 'id-serviciosid-usr'),
    path('servicios/', reclamos.ServiciosView.as_view(),name= 'id-serviciosid-usr'),
    #Detalles servicios
    path('detalleServicio/',reclamos.DetallesServiciosView.as_view(),name= 'id-detallesserviciosid-usr'),
    path('detalleServicio/<str:id>',reclamos.DetallesServiciosView.as_view(),name= 'id-detallesserviciosid-usr'),
    #Documentos servicios
    path('documentos/', reclamos.DocumentosView.as_view(), name='id-documento-usr'),
    path('documentos/<str:id>', reclamos.DocumentosView.as_view(), name='id-documentoid-usr'),
    path('serviciosDocumentos/', reclamos.ServiciosDocumentosView.as_view(),name= 'id-serviciosDocumentosid-usr'),
    path('serviciosDocumentos/<str:id>', reclamos.ServiciosDocumentosView.as_view(),name= 'id-serviciosDocumentosid-usr'),
]
