from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Account, AccountSerializer, Rol, RolSerializer, Reclamo, ReclamoSerializer, Documento, DocumentoSerializer, Evento, EventoSerializer,Planes, PlanesSerializer, Polizas, PolizasSerializer, AgentesVentas, AgentesVentasSerializer, Personas, PersonasSerializer, AsociacionPolizas, AsociacionPolizasSerializer ,UserCreateSerializer , Proveedor, ProveedorSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from django.conf.urls.static import static

import os
import pdfrw
"""
The ContactsView will contain the logic on how to:
 GET, POST, PUT or delete the contacts
"""


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
        peo = request.data
        peo['user_id'] = request.user.id
        serializer = AccountSerializer(data=peo)
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
        peo = request.data
        peo['user_id'] = request.user.id
        serializer = RolSerializer(data=peo)
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

class ReclamoView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, account_id=None):
        if account_id is not None:
            todos = Reclamo.objects.filter(account_id=account_id)
            serializer = ReclamoSerializer(todos, many=True)
            return Response(serializer.data)
        else:
            todos = Reclamo.objects.all()
            serializer = ReclamoSerializer(todos, many=True)
            return Response(serializer.data)

    def post(self, request, account_id ):
        peo = request.data
        peo['account_id'] = account_id
        serializer = ReclamoSerializer(data=peo)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, account_id):
        todo = Reclamo.objects.get(pk=account_id)
        serializer = ReclamoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, account_id):
        Reclamo.objects.get(pk=account_id).delete()
        message = {
            "msg": "Reclamo Borrado"
        }
        return Response(message, status=status.HTTP_200_OK)


class DocumentoView(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, reclamo_id=None, *args, **kwargs):
        if reclamo_id is not None:
            todos = Documento.objects.filter(reclamo_id=reclamo_id)
            serializer = DocumentoSerializer(todos, many=True)
            return Response(serializer.data)
        else:
            todos = Documento.objects.all()
            serializer = DocumentoSerializer(todos, many=True)
            return Response(serializer.data)

    def post(self, request, reclamo_id, *args, **kwargs):
        datos = request.data
        serializer = DocumentoSerializer(data=datos)   
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, reclamo_id):
        todo = Documento.objects.get(pk=reclamo_id)
        serializer = DocumentoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, reclamo_id):
        Documento.objects.get(pk=reclamo_id).delete()
        message = {
            "msg": "documento Borrado"
        }
        return Response(message, status=status.HTTP_200_OK)


class EventoView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, rolName=None):
        if rolName is not None:
            todos = Rol.objects.filter(rolName=rolName)
            serializer = RolSerializer(todos, many=False)
            return Response(serializer.data)
        else:
            todos = Evento.objects.all()
            serializer = EventoSerializer(todos, many=True)
            return Response(serializer.data)

    def post(self, request):
        peo = request.data
        peo['event_id'] = request.user.id
        serializer = EventoSerializer(data=peo)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, name_Account):
        todo = Evento.objects.filter(
            user_id=request.Evento.id, id=request.data['user_id']).first()
        serializer = EventoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ProveedorView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request,):
        todos = Proveedor.objects.all()
        serializer = ProveedorSerializer(todos, many=True)
        return Response(serializer.data)    

class FormularioView(APIView):
    permission_classes = (IsAuthenticated,)


    def get(self,request,reclamo_id):
        
        if reclamo_id is not None:
            RECLAMOS = Reclamo.objects.filter(id=reclamo_id)
            DOCUMENTOS = Documento.objects.filter(reclamo_id=reclamo_id)
            reclamos = RECLAMOS.values('nameReclamo','numpoliza','detalle_diagnostico')[0]
            documentos = DOCUMENTOS.values('tipodoc','nombre_proveedor','numdoc','pago','montodoc')

            data_dict = {
                'detalle1' : '', 'moneda1': '',
                'detalle2' : '', 'moneda2': '',
                'detalle3' : '', 'moneda3': '',
                'detalle4' : '', 'moneda4': '',
                'detalle5' : '', 'moneda5': '',
                'detalle6' : '', 'moneda6': '',
                'monedaTotal': 0,
            }
            for i in range(documentos.count()):
                data_dict['detalle'+str(i+1)] = documentos[i]['tipodoc'] +' - ' + documentos[i]['nombre_proveedor']+' - ' + documentos[i]['numdoc']+' - ' + documentos[i]['pago'] 
                data_dict['moneda'+str(i+1)] = int(documentos[i]['montodoc'])
                data_dict['monedaTotal'] +=  int(documentos[i]['montodoc'])
            
            data_dict.update(reclamos)
            print(data_dict)
            INVOICE_TEMPLATE_PATH = settings.MEDIA_ROOT + '/form.pdf'
            INVOICE_OUTPUT_PATH = settings.MEDIA_ROOT + '/' + reclamo_id +'-' + data_dict['numpoliza'] +'.pdf'
            
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
            "pdf": settings.MEDIA_URL + '/' + reclamo_id +'-' + data_dict['numpoliza'] +'.pdf'
        }
        return Response(message,status=status.HTTP_200_OK)


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
        peo = request.data
        serializer = PlanesSerializer(data=peo)
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
        peo = request.data
        serializer = PolizasSerializer(data=peo)
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
        peo = request.data
        serializer = AgentesVentasSerializer(data=peo)
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
        peo = request.data
        serializer = PersonasSerializer(data=peo)
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
        
class AsociacionPolizasView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, asociacion_id=None):
        if asociacion_id is not None:
            todos = AsociacionPolizas.objects.filter(pk=asociacion_id)
            serializer = AsociacionPolizasSerializer(todos, many=True)
            return Response(serializer.data)
        else:
            todos = AsociacionPolizas.objects.all()
            serializer = AsociacionPolizasSerializer(todos, many=True)
            return Response(serializer.data)

    def post(self, request ):
        peo = request.data
        serializer = AsociacionPolizasSerializer(data=peo)
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

class Registro(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
