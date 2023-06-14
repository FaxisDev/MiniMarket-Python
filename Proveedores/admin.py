from django.contrib import admin
from MiniMarket.admin import admin_site
from .models import Proveedores, NumeroProveedores

# Register your models here.
 
class ProveedoresAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre','email','direccion']
    search_fields = ['nombre','email']

class NumeroProveedoresAdmin(admin.ModelAdmin):
    list_display = ['id', 'id_proveedor','telefono']
    search_fields = ['telefono']


admin_site.register(Proveedores, ProveedoresAdmin)
admin_site.register(NumeroProveedores, NumeroProveedoresAdmin)
