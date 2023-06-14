from django.contrib import admin
from MiniMarket.admin import admin_site
from .models import Productos

 
class ProductosAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'precio', 'stock', 'id_departamento', 'id_marca']
    search_fields = ['nombre']


admin_site.register(Productos, ProductosAdmin)

