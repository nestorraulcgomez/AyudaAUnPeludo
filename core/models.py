
from django.db import models

# Create your models here.

class Servicio (models.Model):

    id_servicio = models.IntegerField(primary_key=True, verbose_name="id_servicio")

    nombre_servicio = models.CharField(max_length=50, verbose_name="servicio")

    def __str__(self):

        return self.nombre_servicio

class Proveedor (models.Model):

    rut = models.IntegerField(primary_key=True, verbose_name="rut_proveedor")

    nombre = models.CharField(max_length=50, verbose_name="nombre_o_razon")

    descripcion = models.CharField(max_length=100, verbose_name="descripcion")

    email = models.CharField(max_length=50, verbose_name="email")

    telefono = models.CharField(max_length=20, verbose_name="telefono")

    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)