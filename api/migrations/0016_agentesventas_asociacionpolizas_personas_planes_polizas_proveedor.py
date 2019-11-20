# Generated by Django 2.2.6 on 2019-11-19 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20191115_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentesVentas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut_agente', models.CharField(default='', max_length=30)),
                ('name_agente', models.CharField(default='', max_length=20)),
                ('lastname_agente', models.CharField(default='', max_length=50)),
                ('telefono_agente', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Planes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_plan', models.CharField(default='', max_length=50)),
                ('sigla_plan', models.CharField(default='', max_length=150)),
                ('Detalle_plan', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupo', models.CharField(default='', max_length=30)),
                ('nombre_proveedor', models.CharField(default='', max_length=150)),
                ('rut_proveedor', models.CharField(default='', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Polizas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_plan', models.CharField(default='', max_length=50)),
                ('nun_poliza', models.CharField(default='', max_length=20)),
                ('estado_poliza', models.CharField(default='', max_length=20)),
                ('inicio_poliza', models.DateField()),
                ('termino_poliza', models.DateField()),
                ('prima_Poliza', models.CharField(default='', max_length=20)),
                ('deducible_Poliza', models.CharField(default='', max_length=20)),
                ('id_Plan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Planes')),
            ],
        ),
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numPolizaLegacy', models.CharField(default='', max_length=30)),
                ('rutCliente', models.CharField(default='', max_length=10)),
                ('nombreCliente', models.CharField(default='', max_length=100)),
                ('apellidoCliente', models.CharField(default='', max_length=150)),
                ('nombrePilaCliente', models.CharField(default='', max_length=100)),
                ('emailPrimarioCliente', models.CharField(default='', max_length=100)),
                ('emailSecundarioCliente', models.CharField(default='', max_length=100)),
                ('direccionParticularCliente', models.CharField(default='', max_length=100)),
                ('direccionComercialCliente', models.CharField(default='', max_length=100)),
                ('nombreConyugeCliente', models.CharField(default='', max_length=100)),
                ('emailConyugeCliente', models.CharField(default='', max_length=100)),
                ('telefonoConyugeCliente', models.CharField(default='', max_length=15)),
                ('telefonoCasaCliente', models.CharField(default='', max_length=15)),
                ('celularCliente', models.CharField(default='', max_length=15)),
                ('nombreSecretariaCliente', models.CharField(default='', max_length=100)),
                ('emailSecretariaCliente', models.CharField(default='', max_length=15)),
                ('isapre', models.CharField(default='', max_length=50)),
                ('fecha_nacimiento_persona', models.DateField()),
                ('numPoliza', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Polizas')),
            ],
        ),
        migrations.CreateModel(
            name='AsociacionPolizas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateField(auto_now=True)),
                ('tipo_asegurado', models.CharField(default='', max_length=5)),
                ('id_agente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.AgentesVentas')),
                ('id_persona', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Personas')),
                ('id_poliza', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Polizas')),
            ],
        ),
    ]
