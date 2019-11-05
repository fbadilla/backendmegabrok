# Generated by Django 2.2.6 on 2019-11-04 17:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20191030_0404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='fecha_nacimiento',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='documento',
            name='datedoc',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]