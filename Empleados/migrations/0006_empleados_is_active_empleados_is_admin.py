# Generated by Django 4.1.7 on 2023-06-22 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Empleados', '0005_rename_clave_empleados_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleados',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='empleados',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
