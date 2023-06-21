from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.utils.timezone import now
# Cargo de empleado
class Cargos(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}. - {self.descripcion}"
    
    class Meta:
        verbose_name_plural = 'Cargos (Puestos)'

class Empleados(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    # Otros campos del modelo
    clave = models.CharField(max_length=128, default='')

    # Este es una llave foranea de la tabla Cargo
    id_cargo = models.ForeignKey(Cargos, on_delete=models.CASCADE)

    #Ultimo Logueo
    last_login = models.DateTimeField(verbose_name='Ultimo logueo', blank=True, null=True)


    def set_password(self, raw_password):
        self.clave = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.clave)
    
    def save(self, *args, **kwargs):
        # Cifrar la contraseña antes de guardarla
        self.clave = make_password(self.clave)
        super().save(*args, **kwargs)
    
    

    def __str__(self):
        return f"{self.id} ({self.nombre})"

    class Meta:
        verbose_name_plural = 'Empleados'

class NumeroEmpleados(models.Model):
    id = models.AutoField(primary_key=True)
    id_empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Numeros Telefonicos (Empleados)'