from django.db import models

from Empleados.models import Empleados
from Productos.models import Productos

# Create your models here.
class Ventas(models.Model):
    id = models.AutoField(primary_key=True)
    descuento = models.FloatField()
    subtotal = models.FloatField()
    total = models.FloatField()
    fecha_venta = models.DateField()
    # Este es una llave foranea de la tabla Empleados
    id_empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} (${self.total}) Empleado: {self.id_empleado}"

    class Meta:
        verbose_name_plural = 'Ventas'

class VentasXProducto(models.Model):

    id = models.AutoField(primary_key=True)
    total = models.FloatField()
    cantidad = models.IntegerField()
    # Este es una llave foranea de la tabla venta
    id_venta = models.ForeignKey(Ventas, on_delete=models.CASCADE)
    # Este es una llave foranea de la tabla productos
    id_producto = models.ForeignKey(Productos, on_delete=models.CASCADE)

    def __str__(self):
        return f"Venta: {self.id_venta}"

    class Meta:
        verbose_name_plural = 'Lista de productos por Venta'
