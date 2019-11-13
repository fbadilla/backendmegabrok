"""
All your application modules and serializers are going to be declared inside this file
"""
from rest_framework import serializers
from django.db import models
from django.contrib.auth.models import User
"""
Define he Contact Entity into your applcation model
"""

class Rol(models.Model):
    rolName= models.CharField(max_length=50, default='')
    description = models.CharField(max_length=150, default='')
    permisos= models.CharField(max_length=150, default='')

class Account(models.Model):
    name_Account= models.CharField(max_length=50, default='')
    fecha_nacimiento = models.CharField(max_length=150, default='')
    phone = models.CharField(max_length=150, default='')
    mail = models.CharField(max_length=150, default='')
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    rol_id = models.ForeignKey(Rol,on_delete=models.CASCADE, null =True)

class Reclamo(models.Model):
    nameReclamo= models.CharField(max_length=50, default='')
    rut = models.CharField(max_length=20, default='')
    numpoliza = models.CharField(max_length=30, default='')
    detalle_diagnostico = models.CharField(max_length=200, default='')
    account_id = models.ForeignKey(Account,on_delete=models.CASCADE,null =True)
    # estado = models.CharField(max_length=20, default='Pendiente')

class Documento(models.Model):
    nombre_proveedor= models.CharField(max_length=50, default='')
    detalle_tratamiento = models.CharField(max_length=150, default='')
    tipodoc = models.CharField(max_length=30, default='')
    numdoc = models.CharField(max_length=30, default='')
    datedoc = models.DateField(auto_now=False, auto_now_add=False,)
    montodoc = models.CharField(max_length=30, default='')
    pago = models.CharField(max_length=30, default='')
    reclamo_id = models.ForeignKey(Reclamo,on_delete=models.CASCADE,null =True)
    docfile = models.FileField(upload_to='post_Files')

class Evento(models.Model):
    name_event= models.CharField(max_length=50, default='')
    date_event = models.DateField(auto_now=False, auto_now_add=False,)
    cost = models.CharField(max_length=150, default='')
    event_id= models.ForeignKey(Account,on_delete=models.CASCADE)
    rolnameID = models.ForeignKey(Rol,on_delete=models.CASCADE, null =True)

# class Cliente(models.Model):
#     numPoliza = models.ForeignKey(Poliza,on_delete=models.CASCADE,null = True)
#     numPolizaLegacy = models.CharField(max_length=30, default='') 
#     rutCliente = models.CharField(max_length=10, default= '')
#     nombreCliente = models.CharField(max_length=100,default='')
#     apellidoCliente = models.CharField(max_length=150, default= '')
#     nombrePilaCliente = models.CharField(max_length=100, default= '')
#     emailPrimarioCliente = models.CharField(max_length=100, default= '')
#     emailSecundarioCliente = models.CharField(max_length=100, default= '')
#     direccionParticularCliente = models.CharField(max_length=100, default= '')
#     direccionComercialCliente = models.CharField(max_length=100, default= '')
#     nombreConyugeCliente = models.CharField(max_length=100, default= '')
#     emailConyugeCliente = models.CharField(max_length=100, default= '')
#     telefonoConyugeCliente = models.CharField(max_length=15, default= '')
#     telefonoCasaCliente  = models.CharField(max_length=15, default= '')
#     celularCliente =  = models.CharField(max_length=15, default= '')
#     nombreSecretariaCliente = models.CharField(max_length=100, default= '')
#     emailSecretariaCliente = models.CharField(max_length=15, default= '')
#     ejecutivoCliente = models.CharField(max_length=50, default='')

# class Poliza(models.Model):
#     numPoliza = models.CharField(max_length=30, default='')
#     fechaInicioPoliza = models.DateField()
#     fechaTerminoPoliza = models.DateField() 
#     companiaPoliza = models.CharField(max_length=5, default='')
#     productoPoliza = models.CharField(max_length=5, default='')
#     primaPoliza = models.CharField(max_length=15, default='')
#     estadoPoliza = models.CharField(max_length=10, default='')

class RolSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rol
        # what fields to include?
        fields = ('id', 'rolName', 'description', 'permisos',)


class AccountSerializer(serializers.ModelSerializer):
    rolName = RolSerializer(many=False, read_only=True)

    class Meta:
        model = Account
        fields = ('id', 'name_Account', 'fecha_nacimiento', 'phone', 'mail', 'user_id', 'rol_id','rolName')

class EventoSerializer(serializers.ModelSerializer):


    class Meta:
        model = Evento
        fields = ('name_event','date_event','cost','event_id','grupo_nameID')

class ReclamoSerializer(serializers.ModelSerializer):


    class Meta:
        model = Reclamo
        fields = ('id','nameReclamo','rut','numpoliza','detalle_diagnostico','account_id')

class DocumentoSerializer(serializers.ModelSerializer):


    class Meta:
        model = Documento
        fields = '__all__'

class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        # there what you want to initial.
        fields = ('id', 'username', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        Account.objects.create(
            name_Account=user.username,
            fecha_nacimiento="",
            phone="",
            mail=user.email,
            user_id=user
        )
        return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password')

