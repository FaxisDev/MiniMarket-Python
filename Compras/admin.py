from django.contrib import admin

from .models import Compras, ComprasXProducto
from MiniMarket.admin import admin_site

class ComprasAdmin(admin.ModelAdmin):
    list_display = ['id', 'descuento', 'subtotal',
                    'total', 'fecha_compra', 'id_empleado']
    list_filter = ['id_empleado', 'fecha_compra']
    search_fields = ['id']


class ComprasXProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'total', 'cantidad', 'id_compra', 'id_producto']
    search_fields = ['id']


admin_site.register(Compras, ComprasAdmin)
admin_site.register(ComprasXProducto, ComprasXProductoAdmin)
