# Generated by Django 4.1.7 on 2023-06-14 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Marcas', '0001_initial'),
        ('Departamentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
                ('stock', models.IntegerField()),
                ('id_departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Departamentos.departamentos')),
                ('id_marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Marcas.marcas')),
            ],
        ),
    ]
