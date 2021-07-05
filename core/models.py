
from django.db import models

# Create your models here.

class Servicio (models.Model):

    id_servicio = models.IntegerField(primary_key=True, verbose_name="ID Servicio")

    nombre_servicio = models.CharField(max_length=50, verbose_name="Servicio")


    def __str__(self):

        return self.nombre_servicio

class Proveedor (models.Model):

    rut = models.CharField(max_length=13 , primary_key=True, verbose_name="Rut proveedor")

    nombre = models.CharField(max_length=50, verbose_name="Nombre")

    descripcion = models.TextField(max_length=100,verbose_name="Descripcion")

    email = models.CharField(max_length=50, verbose_name="Email")

    telefono = models.CharField(max_length=20, verbose_name="Telefono")

    logo = models.ImageField(upload_to = "proveedores",null=True)

    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

    def __str__(self):

        return self.nombre