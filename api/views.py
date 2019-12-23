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

class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, user_id=None):
        todos = Account.objects.filter(user_id=request.user.id).first()
        serializer = AccountSerializer(todos, many=False)
        return Response(serializer.data)

    def put(self, request, user_id=None):
        user = Account.objects.filter(user_id=request.user.id).first()
        serializer = AccountSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AccountView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request,):
        todos = Account.objects.all()
        serializer = AccountSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        data['user_id'] = request.user.id
        serializer = AccountSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        Account.objects.filter(user_id=request.user.id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, name_Account):
        todo = Account.objects.filter(
            user_id=request.user.id, id=request.data['user_id']).first()
        serializer = AccountSerializer(Account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RolView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, rolName=None):
        if rolName is not None:
            todos = Rol.objects.filter(rolName=rolName)
            serializer = RolSerializer(todos, many=False)
            return Response(serializer.data)
        else:
            todos = Rol.objects.all()
            serializer = RolSerializer(todos, many=True)
            return Response(serializer.data)

    def post(self, request):
        data = request.data
        data['user_id'] = request.user.id
        serializer = RolSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, name_Account):
        todo = Rol.objects.filter(
            user_id=request.user.id, id=request.data['user_id']).first()
        serializer = RolSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

class AgentesVentasView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, agente_id=None):
        if agente_id is not None:
            todos = AgentesVentas.objects.filter(pk=agente_id)
            serializer = AgentesVentasSerializer(todos, many=True)
            return Response(serializer.data)
        else:
            todos = AgentesVentas.objects.all()
            serializer = AgentesVentasSerializer(todos, many=True)
            return Response(serializer.data)

    def post(self, request ):
        data = request.data
        serializer = AgentesVentasSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, agente_id):
        todo = AgentesVentas.objects.get(pk=agente_id)
        serializer = AgentesVentasSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, agente_id):
        AgentesVentas.objects.get(pk=agente_id).delete()
        message = {
            "msg": "Agente de ventas Borrada"
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
 


class ReclamosView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, account_id=None):
        if account_id is not None:
            todos = Reclamos.objects.filter(account_id=account_id).annotate(reclamo_id=F('id')).values(
            "reclamo_id", 
            "detalle_diagnostico", 
            "account_id", 
            "date", 
            "name_estado", 
            "num_claim",
            'account_id__name_Account',
            'account_id')
            # serializer = ReclamoSerializer(todos, many=True)
            return Response(todos)
        else:
            todos = Reclamos.objects.all().annotate(reclamo_id=F('id')).values('reclamo_id',
            "asociacion_id__id_poliza__nun_poliza",
            "asociacion_id__id_poliza__numPolizaLegacy",
            'account_id__name_Account', 
            "name_estado",
            "asociacion_id__id_persona__nombre",
            "asociacion_id__id_persona__apellido",
            "asociacion_id__id_persona__rut",
            "detalle_diagnostico",
            "date",
            "num_claim",
            'account_id')
            #serializer = ReclamosSerializer(todos, many=True)
            # return Response(serializer.data)
            return Response(todos)

    # def post(self, request):
    #     data = request.data
    #     serializer = ReclamosSerializer(data=data)   
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def post(self, request, account_id ):
        data = request.data
        data['account_id'] = account_id
        serializer = ReclamosSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, account_id):
        todo = Reclamos.objects.get(pk=account_id)
        serializer = ReclamosSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, account_id):
        Reclamos.objects.get(pk=account_id).delete()
        message = {
            "msg": "Reclamo Borrado"
        }
        return Response(message, status=status.HTTP_200_OK)

class ServiciosView(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser,FileUploadParser)

    def get(self, request, id=None, *args, **kwargs):
        if id is not None:
            todos = Servicios.objects.filter(pk=id)
            serializer = ServiciosSerializer(todos, many=True)
            return Response(serializer.data)
        else:
            todos = Servicios.objects.all()
            serializer = ServiciosSerializer(todos, many=True)
            return Response(serializer.data)
            #return Response(todos)

    def post(self, request, *args, **kwargs ):
        data = request.data
        serializer = ServiciosSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, *args, **kwargs):
        todo = Servicios.objects.get(pk=id)
        serializer = ServiciosSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        Servicios.objects.get(pk=id).delete()
        message = {
            "msg": "Servicio borrado"
        }
        return Response(message, status=status.HTTP_200_OK)


class DetallesServiciosView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        datos = request.data
        serializer = DetallesServiciosSerializer(data=datos)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DocumentosView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id=None):
        if id is not None:
            todos = Documentos.objects.filter(detalle_servicio_id=id)
            serializer = DocumentosSerializer(todos, many=True)
            return Response(serializer.data)
        else:
            todos = Documentos.objects.all()
            serializer = DocumentosSerializer(todos, many=True)
            return Response(serializer.data)

    def post(self, request):
        datos = request.data
        serializer = DocumentosSerializer(data=datos)   
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        todo = Documentos.objects.get(id=request.data['id'],pk = id)
        serializer = DocumentosSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        Documentos.objects.get(pk=id).delete()
        message = {
            "msg": "documento Borrado"
        }
        return Response(message, status=status.HTTP_200_OK)

class ServiciosDocumentosView(APIView):
    permission_classes = (IsAuthenticated,)
    # parser_classes = (MultiPartParser, FormParser,FileUploadParser)
    def get(self, request, id=None):
        if id is not None:
            todos = Servicios.objects.filter(reclamo_id=id).values('id','archivoServicio','proveedor_id','proveedor_id__nombre_proveedor')
            
            for service in todos:
                detalles = DetallesServicios.objects.filter(servicio_id=service['id']).values('id','detalle','pago')
                for detalle in detalles:
                    docs = Documentos.objects.filter(detalle_servicio_id=detalle['id']).values('id','numdoc','tipodoc','datedoc','montodoc')
                    detalle['documentos']= docs
                service['DetalleServicio'] = detalles 
                
            return Response(todos)
        else:
            todos = Reclamos.objects.all().values('id')
            return Response(todos)

class ServiciosProvView(APIView):
    permission_classes = (IsAuthenticated,)
    # parser_classes = (MultiPartParser, FormParser,FileUploadParser)
    def get( self, request, id=None ):
        if id is not None:
            todos = Servicios.objects.filter(reclamo_id=id).annotate(numeroServicio=F('id')).values('proveedor_id','proveedor_id__nombre_proveedor',"numeroServicio")
            for service in todos:
                doc = Documentos.objects.filter(servicio_id=service['numeroServicio']).values('id','numdoc','tipodoc','datedoc','montodoc')
                service['documentos'] = doc 
                serv = Servicios.objects.filter(id=service['numeroServicio']).values('id','detalle','pago','archivoServicio')
                service['servicios'] = serv 
                prov = Proveedores.objects.filter(id=service['numeroServicio']).values('id','nombre_proveedor')
                service['proveedores'] = prov 

            return Response(todos)
        else:
            todos = Servicios.objects.all().values('id')
            return Response(todos)

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


class FormularioView(APIView):   # CLASE PARA OBTENER EL FORMULARIO DE RECLAMACION
    permission_classes = (IsAuthenticated,)

    def get(self,request,reclamo_id):
        if reclamo_id is not None:
            data_dict = {'monedaTotal': 0}

            RECLAMO = Reclamos.objects.filter(id=reclamo_id).annotate(
                nombrePersona=F('asociacion_id__id_persona__nombre'),
                apellidoPersona=F('asociacion_id__id_persona__apellido'),
                numPoliza = F('asociacion_id__id_poliza__nun_poliza')).values(
                'nombrePersona',
                'apellidoPersona',
                'numPoliza',
                'detalle_diagnostico')[0]
            RECLAMO['nombrePaciente'] = RECLAMO['nombrePersona'].strip()+ " " + RECLAMO['apellidoPersona'].strip() 
            data_dict.update(RECLAMO)

            SERVICIOS = Servicios.objects.filter(reclamo_id=reclamo_id).annotate(
                nombreProveedor = F('proveedor_id__nombre_proveedor')).values(
                    'id',
                    'nombreProveedor')
            cont = 1
            for service in SERVICIOS:
                DETALLE_SERVICIO = DetallesServicios.objects.filter(servicio_id=service['id']).values(
                    'id',
                    'servicio_id',
                    'detalle',
                    'pago'
                )

                for detalle in DETALLE_SERVICIO: 
                    numdocs = []
                    monto = 0
                    DOCUMENTOS = Documentos.objects.filter(detalle_servicio_id=detalle['id']).values(
                        'numdoc',
                        'montodoc')
                    for doc in DOCUMENTOS:
                        numdocs.append(doc['numdoc'])
                        monto += int(doc['montodoc']) 
                    numdocs = " - ".join(numdocs)
                    data_dict.update({'detalle'+str(cont):  "{} / {} / {} / {}".format(detalle['detalle'],service['nombreProveedor'],numdocs,detalle['pago']) }) 
                    data_dict.update({'moneda'+str(cont): monto})
                    data_dict['monedaTotal'] +=  monto
                cont+=1

            
            print(data_dict)
            INVOICE_TEMPLATE_PATH = settings.MEDIA_ROOT + '/form.pdf'
            INVOICE_OUTPUT_PATH = settings.MEDIA_ROOT + '/' + reclamo_id +'-' + data_dict['numPoliza'] +'.pdf'
            
            template_pdf = pdfrw.PdfReader(INVOICE_TEMPLATE_PATH)   # se llama a la ruta del pdf 
            
            template_pdf.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
            for page in template_pdf.pages:
                annotations = page['/Annots']
                for annotation in annotations:
                    if annotation['/Subtype'] == '/Widget':
                        if annotation['/T']:
                            key = annotation['/T'][1:-1]
                            if key in data_dict.keys():
                                if type(data_dict[key]) == bool:
                                    if data_dict[key] == True:
                                        annotation.update(pdfrw.PdfDict(
                                            AS=pdfrw.PdfName('Yes')))
                                else:
                                    annotation.update(
                                        pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                                    )
                                    annotation.update(pdfrw.PdfDict(AP=''))
            pdfrw.PdfWriter().write(INVOICE_OUTPUT_PATH, template_pdf)

        message = {
            "pdf": settings.MEDIA_URL + '/' + reclamo_id +'-' + data_dict['numPoliza'] +'.pdf'
        }
        return Response(message,status=status.HTTP_200_OK)


 
class ProveedoresAutocompletarView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request,):
        todos = Proveedores.objects.all().annotate(value=F('id'),label=F('nombre_proveedor')).values('value','label')
        # serializer = ProveedorSerializer(todos, many=True)
        return Response(todos)   


class Registro(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClaimView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        url = "https://mobile.bestdoctorsinsurance.com/spiritapi/api/claim/fileclaim"

        with open(settings.MEDIA_ROOT + '/11-019000021.pdf', "rb") as archivoPDF:
            encoded_string = base64.b64encode(archivoPDF.read())
            archivo = encoded_string.decode('utf-8')

        data = {
            "policyNumber": id,
            "claimantId":105958,
            "ClaimForm":  archivo,
            "extension": "jpg",
            "isBankingInfo": False,
            "comments": "Prueba"}
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Basic QkQxNzYwMy0wMTpOODVGWlJGU1pDMTFSVFNKT0pRRTQwUVFOM0lHRFQxSg==",
            'User-Agent': "PostmanRuntime/7.20.1",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "05bc74c3-ced8-4295-ad5f-844b4e24f692,a34ff8a9-d715-4e45-902f-e9bdde564bb7",
            'Host': "mobile.bestdoctorsinsurance.com",
            'Accept-Encoding': "gzip, deflate",
            'Content-Length': "154",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }
        response = requests.request("POST", url, data=json.dumps(data), headers=headers)
        print(response.text)
        return Response(response.text, status=status.HTTP_200_OK)

class GenerarClaimentIdView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, asociacion_id=None):
        url = "https://mobile.bestdoctorsinsurance.com/spiritapi/api/claim/policymembers/"
        todos = Polizas.objects.all().values('nun_poliza')
        data = open("dataset.json","w")
        headers = {
            'Content-Type': "application/json"
            }
        cont = 0
        for poliza in todos:  
            print(str(cont)+"/"+str(len(todos)))
            if cont == 10 :
                break 
            response = requests.get("https://mobile.bestdoctorsinsurance.com/spiritapi/api/claim/policymembers/"+str(poliza["nun_poliza"]), headers=headers,auth=("BD17603-01","N85FZRFSZC11RTSJOJQE40QQN3IGDT1J"))
            data.write(str("{\"numpoliza\":")+poliza["nun_poliza"]+","+"\"respuesta\":"+response.text+"},")
            cont+=1
        return Response(response.text, status=status.HTTP_200_OK)

class UpdatePolizasView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, asociacion_id=None):
        response = requests.get("https://mobile.bestdoctorsinsurance.com/spiritapi/api/PolicyInfo", auth=("BD17603","N5ZZOQOW8CXVHFJCDWWPW71GXFHXI5IF"))
        data = json.loads(response.text)
        newData = []
        total = len(data)
        cont = 0
        for element in data:
            
            
            nuevo = {}
            nuevo["nun_poliza"] = element.pop("PolicyNumber")
            nuevo["numPolizaLegacy"] = element.pop("LegacyPolicyNumber")
            try:
                nuevo["inicio_poliza"] = datetime.strptime(element.pop("PolicyStartDate"), "%d/%b/%Y").date()
            except:
                nuevo["inicio_poliza"] = None
            try:
                nuevo["termino_poliza"]  = datetime.strptime(element.pop("PolicyEndDate"), "%d/%b/%Y").date()
            except:
                nuevo["termino_poliza"] = None
            nuevo["estado_poliza"] = element.pop("PolicyStatus")
            nombrePlan = element.pop("PlanOption") + " " + element.pop("Plan").split(" ")[1].split("(")[0] 
            nuevo["id_Plan_id"] = Planes.objects.filter(nombre_plan=nombrePlan).values_list("id",flat=True)[0] 
            nuevo["prima_Poliza"] = 12
            nuevo["deducible_Poliza"] = 10
            newData.append(nuevo)
            obj, created = Polizas.objects.update_or_create(nun_poliza =nuevo["nun_poliza"],defaults =nuevo)
            cont+=1
            print(str(cont) + "/" + str(total))
        return Response("Polizas actualizadas correctamente",status=status.HTTP_200_OK)


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