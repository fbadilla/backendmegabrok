from django.db import connection
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import *
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from django.conf.urls.static import static
from django.db.models import F

import os
import pdfrw
import requests
from requests.auth import HTTPBasicAuth
import json 
import simplejson
import base64
import time
from datetime import datetime

class ProveedoresView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, id=None):
        if id is not None:
            todos = Proveedores.objects.filter(grupo_id=id).annotate(
                nombre_grupo = F('grupo_id__nombre_grupo')
            ).values(
                'nombre_grupo',
                'grupo_id',
                'nombre_proveedor',
                'rut_proveedor')
            return Response(todos)
        else:
            todos = Proveedores.objects.all().annotate(
                nombre_grupo = F('grupo_id__nombre_grupo')
            ).values(
                'nombre_grupo',
                'grupo_id',
                'nombre_proveedor',
                'rut_proveedor' )
            return Response(todos)

    def post(self, request):
        datos = request.data
        serializer = ProveedoresSerializer(data=datos)   
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        proveedor = Proveedores.objects.filter(id=request.data["id"]).first()
        serializer = ProveedoresSerializer(proveedor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        Proveedores.objects.get(pk=id).delete()
        message = {
            "msg": "Proveedor Borrado"
        }
        return Response(message, status=status.HTTP_200_OK)


class ProveedoresAutocompletarView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id=None):
        if id is not None:
            todos = Proveedores.objects.filter(grupo_id=id).annotate(value=F('id'),label=F('nombre_proveedor')).values('value','label')
            return Response(todos)
        else:
            todos2 = Proveedores.objects.all().annotate(value=F('id'),label=F('nombre_proveedor')).values('value','label')
            return Response(todos2)  

class GruposView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, id=None):
        if id is not None:
            todos = Grupos.objects.filter(pk=id)
            serializer = GruposSerializer(todos, many=True)
            return Response(serializer.data)
        else:
            todos = Grupos.objects.all()
            serializer = GruposSerializer(todos, many=True)
            return Response(serializer.data)

    def post(self, request):
        datos = request.data
        serializer = GruposSerializer(data=datos)   
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        proveedor = Grupos.objects.filter(id=request.data["id"]).first()
        serializer = GruposSerializer(proveedor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        Grupos.objects.get(pk=id).delete()
        message = {
            "msg": "grupo Borrado"
        }
        return Response(message, status=status.HTTP_200_OK)


class GruposAutocompletarView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request,):
        todos = Grupos.objects.all().annotate(value=F('id'),label=F('nombre_grupo')).values('value','label')
        return Response(todos) 

    def get(self, request, id=None):
        if id is not None:
            todos = Grupos.objects.filter(pk=id).annotate(value=F('id'),label=F('nombre_grupo')).values('value','label')
            return Response(todos)
        else:
            todos2 = Grupos.objects.all().annotate(value=F('id'),label=F('nombre_grupo')).values('value','label')
            return Response(todos2)    
