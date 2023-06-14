from django.db import models

# Create your models here.
class Departamentos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} ({self.nombre})"

    class Meta:
        verbose_name_plural = 'Departamentos'
