from __future__ import unicode_literals

from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50, default="")
    apellido = models.CharField(max_length=50, default="")
    mail = models.CharField(max_length=30, default="")
    web = models.CharField(max_length=30, default="")


class Telefono(models.Model):
    codigo_area = models.IntegerField(default='0000')
    telefono = models.IntegerField(default='0000')
    tipo_choices = (
        ('C','Celular'),
        ('F','Fijo'),
    )
    tipo = models.CharField(max_length=10, choices=tipo_choices)
    proveedor = models.ForeignKey(Proveedor)


class Direccion(models.Model):
    pais = models.CharField(max_length=30, default='')
    provincia = models.CharField(max_length=30, default='')
    ciudad = models.CharField(max_length=30, default='')
    calle = models.CharField(max_length=30, default='')
    altura = models.CharField(max_length=30, default='')
    entre_calle = models.CharField(max_length=30, default='')
    piso = models.CharField(max_length=30, default='')
    depto = models.CharField(max_length=30, default='')
    codigo_postal = models.IntegerField(default='')
    proveedor = models.ForeignKey(Proveedor)
