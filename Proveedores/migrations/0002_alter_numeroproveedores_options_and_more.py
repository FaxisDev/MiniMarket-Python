# Generated by Django 4.1.7 on 2023-06-15 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Proveedores', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='numeroproveedores',
            options={'verbose_name_plural': 'Numeros Telefonicos (Proveedores)'},
        ),
        migrations.AlterModelOptions(
            name='proveedores',
            options={'verbose_name_plural': 'Proveedores'},
        ),
    ]
