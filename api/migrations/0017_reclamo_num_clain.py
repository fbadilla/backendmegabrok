# Generated by Django 2.2.6 on 2019-11-19 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_agentesventas_asociacionpolizas_personas_planes_polizas_proveedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='reclamo',
            name='num_clain',
            field=models.CharField(default='', max_length=30),
        ),
    ]
