# Generated by Django 4.1.7 on 2023-06-14 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Empleados', '0002_empleados_password'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cargos',
            options={'verbose_name_plural': 'Cargos (Puestos)'},
        ),
        migrations.AlterModelOptions(
            name='empleados',
            options={'verbose_name_plural': 'Empleados'},
        ),
        migrations.AlterModelOptions(
            name='numeroempleados',
            options={'verbose_name_plural': 'Numeros Telefonicos (Empleados)'},
        ),
        migrations.RenameField(
            model_name='empleados',
            old_name='password',
            new_name='clave',
        ),
    ]