from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Account, AccountSerializer, Rol, RolSerializer, Reclamo, ReclamoSerializer, Documento, DocumentoSerializer, Evento, Estadoreclamo, EstadoreclamoSerializer, EventoSerializer, UserCreateSerializer
from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework.permissions import IsAuthenticated
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

    def put(self, request,account_id):
        todo = Reclamo.objects.filter(
            account_id=request.data['account_id'], id=request.data['id']).first()
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
        peo = request.data
        peo['reclamo_id'] = reclamo_id
        serializer = DocumentoSerializer(data=peo)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, reclamo_id):
        todo = Documento.objects.filter(
            reclamo_id=request.data['reclamo_id'], id=request.data['id']).first()
        serializer = ReclamoSerializer(todo, data=request.data)
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

class EstadoreclamoView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        todos = Estadoreclamo.objects.all()
        serializer = EstadoreclamoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request ):
        peo = request.data
        serializer = EstadoreclamoSerializer(data=peo)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, estado_id):
        estado_id = Estadoreclamo.objects.get(pk=estado_id)
        serializer = EstadoreclamoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, estado_id):
        Estadoreclamo.objects.get(pk=estado_id).delete()
        message = {
            "msg": "Estado Borrado"
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


class Registro(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
