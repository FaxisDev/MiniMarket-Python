# Generated by Django 4.1.7 on 2023-06-15 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ventas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ventas',
            options={'verbose_name_plural': 'Ventas'},
        ),
        migrations.AlterModelOptions(
            name='ventasxproducto',
            options={'verbose_name_plural': 'Lista de productos por Venta'},
        ),
    ]
