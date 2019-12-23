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
        url = "https://mobile.bestdoctorsinsurance.com/spiritapi/api/claim/policymembers/"
        todos = Polizas.objects.all().values('nun_poliza','id')
        todos = todos[360:]
        total = len(todos)
        cont = 0
        for pol in todos:
            cont+=1
            print(str(cont)+"/"+str(total))
            response = requests.get(url+pol['nun_poliza'] , auth=("BD17603","N5ZZOQOW8CXVHFJCDWWPW71GXFHXI5IF"))
            data = json.loads(response.text)
            for person in data:
                newPersona = {}
                newPersona["ClaimantId"] = person["ClaimantId"]
                try:
                    newPersona["nombre"] = person["ClaimantFirstName"] + " " + person["ClaimantMiddleName"]
                except:
                    newPersona["nombre"] = person["ClaimantFirstName"]
                try:
                    newPersona["apellido"] = person["ClaimantLastName"] + " " + person["ClaimantMotherMaidenName"]
                except:
                    newPersona["apellido"] = person["ClaimantLastName"]

                newPersona["fechaNacimiento"] = datetime.strptime(person["ClaimantDateOfBirth"], "%d/%b/%Y").date()
                persona, createdPersona = Personas.objects.update_or_create(ClaimantId =newPersona["ClaimantId"],defaults = newPersona)
                newAsociacion = {}
                newAsociacion["tipo_asegurado"] = person["ClaimantTypeId"]
                newAsociacion["estado_asegurado"] = person["ClaimantStatusId"]
                newAsociacion["id_persona_id"] = persona.id
                newAsociacion["id_poliza_id"] = pol['id']
                asociacion, createdAsociacion = AsociacionPolizas.objects.update_or_create(id_persona_id = persona.id, id_poliza_id = pol['id'],defaults = newAsociacion)
                print(persona.id)
                print(createdPersona)

        return Response(todos,status=status.HTTP_200_OK)