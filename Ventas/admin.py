from django.contrib import admin
from MiniMarket.admin import admin_site
from .models import Ventas, VentasXProducto  # Register your models here.


class VentasAdmin(admin.ModelAdmin):
    list_display = ['id', 'descuento', 'subtotal',
                    'total', 'fecha_venta', 'id_empleado']
    list_filter = ['id_empleado', 'fecha_venta']
    search_fields = ['id']


class VentasXProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'total', 'cantidad', 'id_venta', 'id_producto']
    search_fields = ['id']


admin_site.register(Ventas, VentasAdmin)
admin_site.register(VentasXProducto, VentasXProductoAdmin)
