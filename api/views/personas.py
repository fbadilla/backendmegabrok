from django.db import connection
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import *
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from django.conf.urls.static import static
from django.db.models import F, Q
import os
import pdfrw
import requests
from requests.auth import HTTPBasicAuth
import json 
import simplejson
import base64
import time
from datetime import datetime


class PersonasView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, persona_id=None):
        if persona_id is not None:
            todos = Personas.objects.filter(pk=persona_id)
            serializer = PersonasSerializer(todos, many=True)
            return Response(serializer.data)
        else:
            todos = Personas.objects.all()
            serializer = PersonasSerializer(todos, many=True)
            return Response(serializer.data)

    def post(self, request ):
        data = request.data
        serializer = PersonasSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, persona_id):
        todo = Personas.objects.get(pk=persona_id)
        serializer = PersonasSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, persona_id):
        Personas.objects.get(pk=persona_id).delete()
        message = {
            "msg": "Persona Borrada"
        }
        return Response(message, status=status.HTTP_200_OK)


class UpdatePersonasView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        print("Solicitando datos de personas")
        url = "https://mobile.bestdoctorsinsurance.com/spiritapi/api/claim/policymembers/"
        todos = Polizas.objects.filter(
            Q(estado_poliza=96005) |
            Q(estado_poliza=96008)
            ).values('nun_poliza','id')
        total = len(todos)
        cont = 1
        for poliza in todos:
            print(str(cont)+"/"+str(total)+ " numero poliza = " + poliza['nun_poliza'] )
            cont+=1
            try:
                response = requests.get(url+poliza['nun_poliza'] , auth=("BD17603","N5ZZOQOW8CXVHFJCDWWPW71GXFHXI5IF"))
                data = json.loads(response.text)
                for person in data:
                    defaults = {'ClaimantId': person["ClaimantId"] }
                    newPersona = {}
                    try:
                        newPersona["nombre"] = person["ClaimantFirstName"] + " " + person["ClaimantMiddleName"]
                    except:
                        newPersona["nombre"] = person["ClaimantFirstName"]
                    try:
                        newPersona["apellido"] = person["ClaimantLastName"] + " " + person["ClaimantMotherMaidenName"]
                    except:
                        newPersona["apellido"] = person["ClaimantLastName"]

            
                    newPersona["fechaNacimiento"] = datetime.strptime(person["ClaimantDateOfBirth"], "%d/%b/%Y").strftime('%Y-%m-%d')

                    persona, createdPersona = Personas.objects.update_or_create(
                        nombre = newPersona["nombre"],
                        apellido= newPersona["apellido"] ,
                        fechaNacimiento = newPersona["fechaNacimiento"],
                        defaults = defaults )

                    newAsociacion = {}
                    newAsociacion["tipo_asegurado"] = person["ClaimantTypeId"]
                    newAsociacion["estado_asegurado"] = person["ClaimantStatusId"]
                    asociacion, createdAsociacion = AsociacionPolizas.objects.update_or_create(
                        id_persona_id = persona.id ,
                        id_poliza_id = poliza['id'],  
                        defaults = newAsociacion)
            except:
                print("no se puede acceder a la poliza")

        return Response(todos,status=status.HTTP_200_OK)