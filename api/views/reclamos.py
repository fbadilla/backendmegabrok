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
import base64

class ReclamosView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, account_id=None):
        if account_id is not None:
            todos = Reclamos.objects.filter(account_id=account_id).annotate(
                reclamo_id=F('id'),
                estado = F('name_estado'),
                numPoliza = F('asociacion_id__id_poliza__nun_poliza'),
                username = F('account_id__name_Account'),
                nombreReclamante = F('asociacion_id__id_persona__nombre'),
                apellidoReclamante = F('asociacion_id__id_persona__apellido'),
                ClaimantId = F('asociacion_id__id_persona__ClaimantId')
            ).values(
                'account_id',
                'reclamo_id',
                'asociacion_id',
                'estado',
                'numPoliza',
                'username', 
                'nombreReclamante',
                'apellidoReclamante',
                "ClaimantId",
                "detalle_diagnostico",
                "date",
                "num_claim")
            return Response(todos)
        else:
            todos = Reclamos.objects.all().annotate(
                reclamo_id=F('id'),
                estado = F('name_estado'),
                numPoliza = F('asociacion_id__id_poliza__nun_poliza'),
                username = F('account_id__name_Account'),
                nombreReclamante = F('asociacion_id__id_persona__nombre'),
                apellidoReclamante = F('asociacion_id__id_persona__apellido'),
                ClaimantId = F('asociacion_id__id_persona__ClaimantId')
            ).values(
                'account_id',
                'reclamo_id',
                'asociacion_id',
                'estado',
                'numPoliza',
                'username', 
                'nombreReclamante',
                'apellidoReclamante',
                "ClaimantId",
                "detalle_diagnostico",
                "date",
                "num_claim")
            return Response(todos)

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
        message = {"msg": "Reclamo Borrado"}
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

    def get(self, request):
            todos = DetallesServicios.objects.all()
            serializer = DetallesServiciosSerializer(todos, many=True)
            return Response(serializer.data)
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

def crearFormulario(reclamo_id=None):
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
            "pdf": settings.MEDIA_URL + reclamo_id +'-' + data_dict['numPoliza'] +'.pdf'
        }
        return message

class FormularioView(APIView):   # CLASE PARA OBTENER EL FORMULARIO DE RECLAMACION
    permission_classes = (IsAuthenticated,)

    def get(self,request,reclamo_id):
        response = crearFormulario(reclamo_id)
        return Response(response,status=status.HTTP_200_OK)

class ClaimView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        urlFile = "https://mobile.bestdoctorsinsurance.com/spiritapi/api/claim/fileclaim"
        urlProvider = "https://mobile.bestdoctorsinsurance.com/spiritapi/api/claim/AddProvider"
        bhiUser = ("BD17603","N5ZZOQOW8CXVHFJCDWWPW71GXFHXI5IF")
        headers = {
            'Content-Type': "application/json"
            }
        
        if not request.data['servicios']:
            message =  {'reason': 'No existe ningun servicio'}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)
        if request.data['reclamo']['estado'] == 'Enviado':
            message =  {'reason': 'El reclamo ya ha sido enviado'}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)

        reclamo_id = str(request.data['reclamo']['reclamo_id'])
        numPoliza =request.data['reclamo']['numPoliza']
        crearFormulario(reclamo_id)
        rutaFormulario = "{}/{}-{}.pdf".format(settings.MEDIA_ROOT,reclamo_id,numPoliza)
        
        with open(rutaFormulario, "rb") as archivoPDF:
            encoded_string = base64.b64encode(archivoPDF.read())
            formulario = encoded_string.decode('utf-8')
        
        dataFile = {
            "policyNumber": numPoliza,
            "claimantId": request.data['reclamo']['ClaimantId'],
            "ClaimForm":  formulario,
            "extension": "pdf",
            "isBankingInfo": False,
            "comments": "Prueba"}
        
        response = requests.post(urlFile, data=json.dumps(dataFile), headers=headers,auth=bhiUser)
        responseFile = json.loads(response.text)
        claimId = responseFile["ClaimId"] 
        print(claimId)

        for service in request.data['servicios']:
            if 'documentos' not in service:
                message =  {'reason': 'Ingrese documentos en los servicios'}
                return Response(message,status=status.HTTP_400_BAD_REQUEST)

            archivoServicio = service['archivoServicio']
            nameFileProv, extFileProv = os.path.splitext(settings.MEDIA_ROOT + '/' + archivoServicio) 
            try:
                with open(nameFileProv+extFileProv, "rb") as archivoPDF:
                    encoded_string = base64.b64encode(archivoPDF.read())
                    proveedor = encoded_string.decode('utf-8')
            except:
                message =  {'reason': 'Verifique los archivos de los servicios'}
                return Response(message,status=status.HTTP_400_BAD_REQUEST)
            
            dataProvider = {
            "ClaimId" : responseFile["ClaimId"],
            "BillingProviderName": service["proveedor_id__nombre_proveedor"],
            "TypeOfService": [],
            "InsideUS": False,
            "Bill": proveedor,
            "Extension": extFileProv
            }
            for detalle in service['DetalleServicio']:
                dataProvider['TypeOfService'].append(detalle['detalle'])
            dataProvider['TypeOfService'] = (" - ").join(dataProvider['TypeOfService'])
            
            response = requests.post(urlProvider,data =json.dumps(dataProvider),headers = headers,auth=bhiUser)
            responseProvider = response.text
        
        urlSubmit = "https://mobile.bestdoctorsinsurance.com/spiritapi/api/claim/submitclaim/" + str(claimId)
        dataSubmit = {
            "ClaimId": claimId
        }
        
        response = requests.post(urlSubmit,data = json.dumps(dataSubmit),headers = headers,auth = bhiUser)
        data = {
            'account_id' : request.data['reclamo']['account_id'],
            'date' : request.data['reclamo']['date'],
            'detalle_diagnostico' : request.data['reclamo']['detalle_diagnostico'],
            'name_estado' : 'Enviado',
            'asociacion_id' : request.data['reclamo']['asociacion_id'],
            'num_claim' : claimId
        }
        reclamo = Reclamos.objects.get(pk=request.data['reclamo']['reclamo_id'])
        serializer = ReclamosSerializer(reclamo, data=data)
        if serializer.is_valid():
            serializer.save()

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
            response = requests.get("https://mobile.bestdoctorsinsurance.com/spiritapi/api/claim/policymembers/"+str(poliza["nun_poliza"]), headers=headers,auth=("BD17603","N5ZZOQOW8CXVHFJCDWWPW71GXFHXI5IF"))
            data.write(str("{\"numpoliza\":")+poliza["nun_poliza"]+","+"\"respuesta\":"+response.text+"},")
            cont+=1
        return Response(response.text, status=status.HTTP_200_OK)