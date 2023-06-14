from django.contrib import admin
from MiniMarket.admin import admin_site
from .models import Marcas
 
class MarcasAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre','id_proveedor']
    search_fields = ['nombre']


admin_site.register(Marcas, MarcasAdmin)

