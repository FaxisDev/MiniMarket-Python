from django.contrib import admin
from MiniMarket.admin import admin_site

# Register your models here.
from .models import Departamentos

class DepartamentosAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'descripcion']
    search_fields = ['nombre']


admin_site.register(Departamentos, DepartamentosAdmin)
