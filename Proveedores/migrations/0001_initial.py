# Generated by Django 4.1.7 on 2023-06-14 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NumeroProveedores',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('telefono', models.CharField(max_length=100)),
                ('id_proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Proveedores.proveedores')),
            ],
        ),
    ]
