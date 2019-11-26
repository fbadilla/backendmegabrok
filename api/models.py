from rest_framework import serializers
from django.db import models
from django.contrib.auth.models import User
import datetime

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
    date = models.DateField(auto_now=True)
    name_estado= models.CharField(max_length=50, default='Pendiente')
    num_claim= models.CharField(max_length=30, default='',blank=True)

class Documento(models.Model):
    nombre_proveedor= models.CharField(max_length=50, default='')
    detalle_tratamiento = models.CharField(max_length=150, default='')
    tipodoc = models.CharField(max_length=30, default='')
    numdoc = models.CharField(max_length=30, default='')
    datedoc = models.DateField(auto_now=False, auto_now_add=False,)
    montodoc = models.CharField(max_length=30, default='')
    pago = models.CharField(max_length=30, default='')
    reclamo_id = models.ForeignKey(Reclamo,on_delete=models.CASCADE,null =True)
    docfile = models.FileField(upload_to='post_Files',blank = True,null =True,default= None)

class Evento(models.Model):
    name_event= models.CharField(max_length=50, default='')
    date_event = models.DateField(auto_now=False, auto_now_add=False,)
    cost = models.CharField(max_length=150, default='')
    event_id= models.ForeignKey(Account,on_delete=models.CASCADE)
    rolnameID = models.ForeignKey(Rol,on_delete=models.CASCADE, null =True)

class Proveedor(models.Model):
    grupo = models.CharField(max_length=30, default='')
    nombre_proveedor = models.CharField(max_length=150, default='')
    rut_proveedor = models.CharField(max_length=15, default='')

class Planes(models.Model):
    nombre_plan= models.CharField(max_length=50, default='')
    sigla_plan = models.CharField(max_length=150, default='')
    Detalle_plan = models.CharField(max_length=200, default='')

class Polizas(models.Model):
    id_Plan = models.ForeignKey(Planes,on_delete=models.CASCADE, null =True)
    nun_poliza = models.CharField(max_length=20, default='')
    numPolizaLegacy = models.CharField(max_length=30, default='') 
    estado_poliza = models.CharField(max_length=20, default='')
    inicio_poliza = models.DateField(auto_now=False, auto_now_add=False)
    termino_poliza = models.DateField(auto_now=False, auto_now_add=False)
    prima_Poliza = models.CharField(max_length=20, default='')
    deducible_Poliza = models.CharField(max_length=20, default='')

class AgentesVentas(models.Model):
    rut_agente= models.CharField(max_length=30, default='')
    name_agente = models.CharField(max_length=20, default='')
    lastname_agente = models.CharField(max_length=50, default='')
    telefono_agente = models.CharField(max_length=10, default='')
    cod_agente = models.CharField(max_length=25, default='')

class Personas(models.Model): 
    rutCliente = models.CharField(max_length=10, default= '')
    nombreCliente = models.CharField(max_length=100,default='')
    apellidoCliente = models.CharField(max_length=150, default= '')
    nombrePilaCliente = models.CharField(max_length=100, default= '')
    emailPrimarioCliente = models.CharField(max_length=100, default= '')
    emailSecundarioCliente = models.CharField(max_length=100, default= '')
    direccionParticularCliente = models.CharField(max_length=100, default= '')
    direccionComercialCliente = models.CharField(max_length=100, default= '')
    nombreConyugeCliente = models.CharField(max_length=100, default= '')
    emailConyugeCliente = models.CharField(max_length=100, default= '')
    telefonoConyugeCliente = models.CharField(max_length=15, default= '')
    telefonoCasaCliente  = models.CharField(max_length=15, default= '')
    telefonoOficina  = models.CharField(max_length=15, default= '')
    celularCliente =  models.CharField(max_length=15, default= '')
    nombreSecretariaCliente = models.CharField(max_length=100, default= '')
    emailSecretariaCliente = models.CharField(max_length=15, default= '')
    isapre = models.CharField(max_length=50, default='')
    fecha_nacimiento_persona = models.DateField(auto_now=False, auto_now_add=False,)
    tipo_asegurado= models.CharField(max_length=5, default='')

class AsociacionPolizas(models.Model):
    id_poliza = models.ForeignKey(Polizas,on_delete=models.CASCADE,null =True)
    id_persona = models.ForeignKey(Personas,on_delete=models.CASCADE,null =True)
    id_agente = models.ForeignKey(AgentesVentas,on_delete=models.CASCADE,null =True)
    fecha_creacion = models.DateField(auto_now=True)

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
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

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields= ('grupo','nombre_proveedor','rut_proveedor')

class ReclamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reclamo
        fields = '__all__'

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = '__all__'

class PlanesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planes
        fields = '__all__'

class PolizasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polizas
        fields = '__all__'

class AgentesVentasSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentesVentas
        fields = '__all__'

class PersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personas
        fields = '__all__'

class AsociacionPolizasSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsociacionPolizas
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