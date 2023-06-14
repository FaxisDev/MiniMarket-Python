from django.db import models

from Empleados.models import Empleados
from Productos.models import Productos

# Create your models here.
class Compras(models.Model):
    id = models.AutoField(primary_key=True)
    descuento = models.FloatField()
    subtotal = models.FloatField()
    total = models.FloatField()
    fecha_compra = models.DateField()
    # Este es una llave foranea de la tabla Empleados
    id_empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} (${self.total}) Empleado: {self.id_empleado}"

    class Meta:
        verbose_name_plural = 'Compras'


class ComprasXProducto(models.Model):
    id = models.AutoField(primary_key=True)
    total = models.FloatField()
    cantidad = models.IntegerField()
    # Este es una llave foranea de la tabla venta
    id_compra = models.ForeignKey(Compras, on_delete=models.CASCADE)
    # Este es una llave foranea de la tabla productos
    id_producto = models.ForeignKey(Productos, on_delete=models.CASCADE)

    def __str__(self):
        return f"Compra: {self.id_compra}"

    class Meta:
        verbose_name_plural = 'Lista de productos por Compra'
