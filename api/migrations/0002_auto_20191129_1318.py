# Generated by Django 2.2.6 on 2019-11-29 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipodoc', models.CharField(default='', max_length=30)),
                ('numdoc', models.CharField(default='', max_length=30)),
                ('datedoc', models.DateField()),
                ('montodoc', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Reclamos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('detalle_diagnostico', models.CharField(default='', max_length=200)),
                ('name_estado', models.CharField(default='Pendiente', max_length=50)),
                ('num_claim', models.CharField(blank=True, default='', max_length=30)),
                ('account_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.CharField(default='', max_length=200)),
                ('pago', models.CharField(default='', max_length=30)),
                ('archivoServicio', models.FileField(blank=True, default=None, null=True, upload_to='post_Files')),
            ],
        ),
        migrations.RemoveField(
            model_name='evento',
            name='event_id',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='rolnameID',
        ),
        migrations.RemoveField(
            model_name='reclamo',
            name='account_id',
        ),
        migrations.RenameField(
            model_name='personas',
            old_name='apellidoCliente',
            new_name='apellido',
        ),
        migrations.RenameField(
            model_name='personas',
            old_name='celularCliente',
            new_name='celular',
        ),
        migrations.RenameField(
            model_name='personas',
            old_name='direccionComercialCliente',
            new_name='direccionComercial',
        ),
        migrations.RenameField(
            model_name='personas',
            old_name='direccionParticularCliente',
            new_name='direccionParticular',
        ),
        migrations.RenameField(
            model_name='personas',
            old_name='emailConyugeCliente',
            new_name='emailConyuge',
        ),
        migrations.RenameField(
            model_name='personas',
            old_name='emailPrimarioCliente',
            new_name='emailPrimario',
        ),
        migrations.RenameField(
            model_name='personas',
            old_name='emailSecretariaCliente',
            new_name='emailSecretaria',
        ),
        migrations.RenameField(
            model_name='personas',
            old_name='emailSecundarioCliente',
            new_name='emailSecundario',
        ),
        migrations.RenameField(
            model_name='personas',
            old_name='fecha_nacimiento_persona',
            new_name='fechaNacimiento',
        ),
        migrations.RenameField(
            model_name='personas',
            old_name='nombreCliente',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='personas',
            old_name='nombreConyugeCliente',
            new_name='nombreConyuge',
        ),
        migrations.RenameField(
            model_name='personas',
            old_name='nombrePilaCliente',
            new_name='nombrePila',
        ),
        migrations.RenameField(
            model_name='personas',
            old_name='nombreSecretariaCliente',
            new_name='nombreSecretaria',
        ),
        migrations.RenameField(
            model_name='personas',
            old_name='rutCliente',
            new_name='rut',
        ),
        migrations.RenameField(
            model_name='personas',
            old_name='telefonoCasaCliente',
            new_name='telefonoCasa',
        ),
        migrations.RenameField(
            model_name='personas',
            old_name='telefonoConyugeCliente',
            new_name='telefonoConyuge',
        ),
        migrations.AlterField(
            model_name='asociacionpolizas',
            name='id_persona',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Personas'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='asociacionpolizas',
            name='id_poliza',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='api.Polizas'),
            preserve_default=False,
        ),
        migrations.RenameModel(
            old_name='Proveedor',
            new_name='Proveedores',
        ),
        migrations.DeleteModel(
            name='Documento',
        ),
        migrations.DeleteModel(
            name='Evento',
        ),
        migrations.DeleteModel(
            name='Reclamo',
        ),
        migrations.AddField(
            model_name='servicios',
            name='proveedor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Proveedores'),
        ),
        migrations.AddField(
            model_name='servicios',
            name='reclamo_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Reclamos'),
        ),
        migrations.AddField(
            model_name='reclamos',
            name='asociacion_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.AsociacionPolizas'),
        ),
        migrations.AddField(
            model_name='documentos',
            name='servicio_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Servicios'),
        ),
    ]