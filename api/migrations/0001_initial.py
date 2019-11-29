# Generated by Django 2.2.7 on 2019-11-28 16:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_Account', models.CharField(default='', max_length=50)),
                ('fecha_nacimiento', models.CharField(default='', max_length=150)),
                ('phone', models.CharField(default='', max_length=150)),
                ('mail', models.CharField(default='', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='AgentesVentas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut_agente', models.CharField(default='', max_length=30)),
                ('name_agente', models.CharField(default='', max_length=20)),
                ('lastname_agente', models.CharField(default='', max_length=50)),
                ('telefono_agente', models.CharField(default='', max_length=10)),
                ('cod_agente', models.CharField(default='', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('telefonoOficina', models.CharField(default='', max_length=15)),
                ('celularCliente', models.CharField(default='', max_length=15)),
                ('nombreSecretariaCliente', models.CharField(default='', max_length=100)),
                ('emailSecretariaCliente', models.CharField(default='', max_length=15)),
                ('isapre', models.CharField(default='', max_length=50)),
                ('fecha_nacimiento_persona', models.DateField()),
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
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rolName', models.CharField(default='', max_length=50)),
                ('description', models.CharField(default='', max_length=150)),
                ('permisos', models.CharField(default='', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Reclamo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameReclamo', models.CharField(default='', max_length=50)),
                ('rut', models.CharField(blank=True, default='', max_length=20)),
                ('numpoliza', models.CharField(default='', max_length=30)),
                ('detalle_diagnostico', models.CharField(default='', max_length=200)),
                ('date', models.DateField(auto_now=True)),
                ('name_estado', models.CharField(default='Pendiente', max_length=50)),
                ('num_claim', models.CharField(blank=True, default='', max_length=30)),
                ('account_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Polizas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nun_poliza', models.CharField(default='', max_length=20)),
                ('numPolizaLegacy', models.CharField(default='', max_length=30)),
                ('estado_poliza', models.CharField(default='', max_length=20)),
                ('inicio_poliza', models.DateField()),
                ('termino_poliza', models.DateField()),
                ('prima_Poliza', models.CharField(default='', max_length=20)),
                ('deducible_Poliza', models.CharField(default='', max_length=20)),
                ('id_Plan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Planes')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_event', models.CharField(default='', max_length=50)),
                ('date_event', models.DateField()),
                ('cost', models.CharField(default='', max_length=150)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Account')),
                ('rolnameID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Rol')),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle_tratamiento', models.CharField(default='', max_length=150)),
                ('tipodoc', models.CharField(default='', max_length=30)),
                ('numdoc', models.CharField(default='', max_length=30)),
                ('datedoc', models.DateField()),
                ('montodoc', models.CharField(default='', max_length=30)),
                ('pago', models.CharField(default='', max_length=30)),
                ('docfile', models.FileField(blank=True, default=None, null=True, upload_to='post_Files')),
                ('proveedor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Proveedor')),
                ('reclamo_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Reclamo')),
            ],
        ),
        migrations.CreateModel(
            name='AsociacionPolizas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateField(auto_now=True)),
                ('tipo_asegurado', models.CharField(default='', max_length=10)),
                ('id_agente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.AgentesVentas')),
                ('id_persona', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Personas')),
                ('id_poliza', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Polizas')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='rol_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Rol'),
        ),
        migrations.AddField(
            model_name='account',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
