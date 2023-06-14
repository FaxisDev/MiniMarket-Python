from django.db import models

from Proveedores.models import Proveedores

# Create your models here.
class Marcas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    # Este es una llave foranea de la tabla Proveedor
    id_proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} ({self.nombre})"

    class Meta:
        verbose_name_plural = 'Marcas (Productos)'