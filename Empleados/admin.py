from django.contrib import admin
from MiniMarket.admin import admin_site
# Register your models here.
from .models import Empleados, Cargos, NumeroEmpleados

class EmpleadosAdmin(admin.ModelAdmin):
    verbose_name_plural = 'Empleados'
    list_display = ['id', 'nombre', 'email']
    search_fields = ['id', 'email']


class NumeroEmpleadosAdmin(admin.ModelAdmin):
    list_display = ['id', 'id_empleado', 'telefono']
    list_filter = ['id_empleado']
    search_fields = ['telefono']

class CargosAdmin(admin.ModelAdmin):
    list_display = ['id', 'descripcion']


admin_site.register(Empleados, EmpleadosAdmin)
admin_site.register(Cargos,CargosAdmin)
admin_site.register(NumeroEmpleados, NumeroEmpleadosAdmin)
