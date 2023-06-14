from django.db import models
from Departamentos.models import Departamentos
from Marcas.models import Marcas

# Create your models here.
class Productos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    stock = models.IntegerField()
    id_departamento = models.ForeignKey(Departamentos, on_delete=models.CASCADE)
    id_marca = models.ForeignKey(Marcas, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} ({self.nombre})"

    class Meta:
        verbose_name_plural = 'Productos'