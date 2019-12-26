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


class PlanesView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, plan_id=None):
        if plan_id is not None:
            todos = Planes.objects.filter(pk=plan_id)
            serializer = PlanesSerializer(todos, many=True)
            return Response(serializer.data)
        else:
            todos = Planes.objects.all()
            serializer = PlanesSerializer(todos, many=True)
            return Response(serializer.data)

    def post(self, request ):
        data = request.data
        serializer = PlanesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, plan_id):
        todo = Planes.objects.get(pk=plan_id)
        serializer = PlanesSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, plan_id):
        Planes.objects.get(pk=plan_id).delete()
        message = {
            "msg": "Plan Borrado"
        }
        return Response(message, status=status.HTTP_200_OK)

class PolizasView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, Poliza_id=None):
        if Poliza_id is not None:
            todos = Polizas.objects.filter(pk=Poliza_id)
            serializer = PolizasSerializer(todos, many=True)
            return Response(serializer.data)
        else:
            todos = Polizas.objects.all()
            serializer = PolizasSerializer(todos, many=True)
            return Response(serializer.data)

    def post(self, request ):
        data = request.data
        serializer = PolizasSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, Poliza_id):
        todo = Polizas.objects.get(pk=Poliza_id)
        serializer = PolizasSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, Poliza_id):
        Polizas.objects.get(pk=Poliza_id).delete()
        message = {
            "msg": "Poliza Borrada"
        }
        return Response(message, status=status.HTTP_200_OK)

class AsociacionPolizasView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, asociacion_id=None):
        if asociacion_id is not None:
            todos = AsociacionPolizas.objects.filter(pk=asociacion_id)
            serializer = AsociacionPolizasSerializer(todos, many=True)
            return Response(serializer.data)
        else:
            todos = AsociacionPolizas.objects.all().values('id','id_persona_id','id_persona__rut','id_persona__nombre','id_persona__apellido','tipo_asegurado','id_poliza__nun_poliza','id_poliza__numPolizaLegacy')
            return Response(todos)

    def post(self, request ):
        data = request.data
        serializer = AsociacionPolizasSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, asociacion_id):
        todo = AsociacionPolizas.objects.get(pk=asociacion_id)
        serializer = AsociacionPolizasSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, asociacion_id):
        AsociacionPolizas.objects.get(pk=asociacion_id).delete()
        message = {
            "msg": "asociacion  Borrada"
        }
        return Response(message, status=status.HTTP_200_OK)


class UpdatePolizasView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, asociacion_id=None):
        print("solicitando polizas..")
        response = requests.get("https://mobile.bestdoctorsinsurance.com/spiritapi/api/PolicyInfo", auth=("BD17603","N5ZZOQOW8CXVHFJCDWWPW71GXFHXI5IF"))
        data = json.loads(response.text)
        total = len(data)
        cont = 1
        for element in data:
            defaults = {}
            defaults["nun_poliza"] = element["PolicyNumber"]
            defaults["numPolizaLegacy"] = element["LegacyPolicyNumber"]
            try:
                defaults["inicio_poliza"] = datetime.strptime(element["PolicyStartDate"], "%d/%b/%Y").strftime('%Y-%m-%d')
            except:
                defaults["inicio_poliza"] = None
            try:
                defaults["termino_poliza"]  = datetime.strptime(element["PolicyEndDate"], "%d/%b/%Y").strftime('%Y-%m-%d')
            except:
                defaults["termino_poliza"] = None
            
            defaults["estado_poliza"] = element["PolicyStatus"]
            detallePlan = element["Plan"][7:-32] 
            defaults["id_Plan_id"] = getattr(Planes.objects.get(Detalle_plan = detallePlan),'id')
            defaults["prima_Poliza"] = None
            defaults["deducible_Poliza"] = None
            poliza, created = Polizas.objects.update_or_create(
                nun_poliza =element["PolicyNumber"],
                defaults =defaults)
            print(str(cont) + "/" + str(total))
            cont+=1
        return Response("Polizas actualizadas correctamente",status=status.HTTP_200_OK)