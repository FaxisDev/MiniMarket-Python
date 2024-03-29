# Generated by Django 4.1.7 on 2023-06-14 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('id_cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empleados.cargos')),
            ],
        ),
        migrations.CreateModel(
            name='NumeroEmpleados',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('telefono', models.CharField(max_length=100)),
                ('id_empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empleados.empleados')),
            ],
        ),
    ]
