# Generated by Django 2.2.7 on 2019-11-20 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_remove_polizas_nombre_plan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reclamo',
            old_name='num_clain',
            new_name='num_claim',
        ),
    ]