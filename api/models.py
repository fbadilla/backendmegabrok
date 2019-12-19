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

class Personas(models.Model): 
    ClaimantId = models.IntegerField(null=True)
    rut = models.CharField(max_length=10, default= '')
    nombre = models.CharField(max_length=100,default='')
    apellido = models.CharField(max_length=150, default= '')
    nombrePila = models.CharField(max_length=100, default= '')
    emailPrimario = models.CharField(max_length=100, default= '')
    emailSecundario = models.CharField(max_length=100, default= '')
    direccionParticular = models.CharField(max_length=100, default= '')
    direccionComercial = models.CharField(max_length=100, default= '')
    nombreConyuge = models.CharField(max_length=100, default= '')
    emailConyuge = models.CharField(max_length=100, default= '')
    telefonoConyuge = models.CharField(max_length=15, default= '')
    telefonoCasa  = models.CharField(max_length=15, default= '')
    telefonoOficina  = models.CharField(max_length=15, default= '')
    celular =  models.CharField(max_length=15, default= '')
    nombreSecretaria = models.CharField(max_length=100, default= '')
    emailSecretaria = models.CharField(max_length=15, default= '')
    isapre = models.CharField(max_length=50, default='')
    fechaNacimiento = models.DateField(auto_now=False, auto_now_add=False,)

class Planes(models.Model):
    nombre_plan= models.CharField(max_length=50, default='')
    sigla_plan = models.CharField(max_length=150, default='')
    Detalle_plan = models.CharField(max_length=200, default='')

class Polizas(models.Model):
    id_Plan = models.ForeignKey(Planes,on_delete=models.CASCADE, null =True)
    nun_poliza = models.CharField(max_length=20, default='')
    numPolizaLegacy = models.CharField(max_length=30, default='',null=True) 
    estado_poliza = models.CharField(max_length=20, default='')
    inicio_poliza = models.DateField(auto_now=False, auto_now_add=False,null=True)
    termino_poliza = models.DateField(auto_now=False, auto_now_add=False,null=True)
    prima_Poliza = models.CharField(max_length=20, default='')
    deducible_Poliza = models.CharField(max_length=20, default='')

class AgentesVentas(models.Model):
    rut_agente= models.CharField(max_length=30, default='')
    name_agente = models.CharField(max_length=20, default='')
    lastname_agente = models.CharField(max_length=50, default='')
    telefono_agente = models.CharField(max_length=10, default='')
    cod_agente = models.CharField(max_length=25, default='')

class AsociacionPolizas(models.Model):
    id_poliza = models.ForeignKey(Polizas,on_delete=models.CASCADE)
    id_persona = models.ForeignKey(Personas,on_delete=models.CASCADE)
    id_agente = models.ForeignKey(AgentesVentas,on_delete=models.CASCADE,null =True)
    fecha_creacion = models.DateField(auto_now=True)
    tipo_asegurado= models.IntegerField(null = True)
    estado_asegurado = models.IntegerField(null=True)

class Reclamos(models.Model):
    account_id = models.ForeignKey(Account,on_delete=models.CASCADE,null =True)
    asociacion_id = models.ForeignKey(AsociacionPolizas,on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    detalle_diagnostico = models.CharField(max_length=200, default='')
    name_estado= models.CharField(max_length=50, default='Pendiente')
    num_claim= models.CharField(max_length=30, default='',blank=True)

class Proveedores(models.Model):
    grupo = models.CharField(max_length=30, default='',blank=True)
    nombre_proveedor = models.CharField(max_length=150, default='')
    rut_proveedor = models.CharField(max_length=15, default='')

class Servicios(models.Model):
    reclamo_id = models.ForeignKey(Reclamos,on_delete=models.CASCADE)
    proveedor_id = models.ForeignKey(Proveedores,on_delete=models.CASCADE)
    archivoServicio = models.FileField(upload_to='post_Files',blank = True,null =True,default= None)

class DetallesServicios(models.Model):
    servicio_id = models.ForeignKey(Servicios,on_delete=models.CASCADE)
    detalle = models.CharField(max_length=200, default='')
    pago = models.CharField(max_length=30, default='')
    
class Documentos(models.Model):
    detalle_servicio_id = models.ForeignKey(DetallesServicios,on_delete=models.CASCADE,null=True)
    tipodoc = models.CharField(max_length=30, default='')
    numdoc = models.CharField(max_length=30, default='')
    datedoc = models.DateField(auto_now=False, auto_now_add=False,)
    montodoc = models.CharField(max_length=30, default='')


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ('id', 'rolName', 'description', 'permisos',)


class AccountSerializer(serializers.ModelSerializer):
    rolName = RolSerializer(many=False, read_only=True)

    class Meta:
        model = Account
        fields = ('id', 'name_Account', 'fecha_nacimiento', 'phone', 'mail', 'user_id', 'rol_id','rolName')

class PersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personas
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

class AsociacionPolizasSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsociacionPolizas
        fields = '__all__'

class ReclamosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reclamos
        fields = '__all__'

class ProveedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedores
        fields= '__all__'

class ServiciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicios
        fields = '__all__'

class DetallesServiciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallesServicios
        fields = '__all__'

class DocumentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documentos
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