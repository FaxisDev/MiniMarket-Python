from django.db import models

# Create your models here.
class Proveedores(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} ({self.nombre})"

    class Meta:
        verbose_name_plural = 'Proveedores'
    



class NumeroProveedores(models.Model):
    id = models.AutoField(primary_key=True)
    id_proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} ({self.telefono})"

    class Meta:
        verbose_name_plural = 'Numeros Telefonicos (Proveedores)'