# Generated by Django 2.2.6 on 2019-11-04 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20191104_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='datedoc',
            field=models.DateField(),
        ),
    ]