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
    def get(self,request,):
        todos = Proveedores.objects.all()
        serializer = ProveedoresSerializer(todos, many=True)
        return Response(serializer.data)   

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

    def get(self,request,):
        todos = Proveedores.objects.all().annotate(value=F('id'),label=F('nombre_proveedor')).values('value','label')
        # serializer = ProveedorSerializer(todos, many=True)
        return Response(todos)   
