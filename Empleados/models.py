from django.db import models
from django.contrib.auth.hashers import make_password, check_password

from django.contrib.auth.models import AbstractBaseUser
# Cargo de empleado


class Cargos(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}. - {self.descripcion}"

    class Meta:
        verbose_name_plural = 'Cargos (Puestos)'


class Empleados(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    # Otros campos del modelo
    password = models.CharField(max_length=128, default='')

    # Este es una llave foranea de la tabla Cargo
    id_cargo = models.ForeignKey(Cargos, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    # Ultimo Logueo
    last_login = models.DateTimeField(
        verbose_name='Ultimo logueo', blank=True, null=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def save(self, *args, **kwargs):
        # Cifrar la contraseña antes de guardarla y verificar que no cambie
        if self.pk:
            pass_get = Empleados.objects.get(id=self.pk)
            if self.password != pass_get.password:
                self.password = make_password(self.password)
        super().save(*args, **kwargs)

    @property
    def is_staff(self):
        return self.is_admin

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
