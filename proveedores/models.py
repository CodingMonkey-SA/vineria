from __future__ import unicode_literals

from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50, default="", blank=True)
    apellido = models.CharField(max_length=50, default="", blank=True)
    telefono_fijo = models.CharField(max_length=30, default="", blank=True)
    celular = models.CharField(max_length=30, default="", blank=True)
    pais = models.CharField(max_length=30, default="", blank=True)
    provincia = models.CharField(max_length=30, default="", blank=True)
    ciudad = models.CharField(max_length=30, default="", blank=True)
    calle = models.CharField(max_length=30, default="", blank=True)
    altura = models.CharField(max_length=30, default="", blank=True)
    entre_calle = models.CharField(max_length=30, default="", blank=True)
    piso = models.CharField(max_length=30, default="", blank=True)
    depto = models.CharField(max_length=30, default="", blank=True)
    codigo_postal = models.CharField(max_length=30, default="", blank=True)
    mail = models.CharField(max_length=30, default="", blank=True)
    web = models.CharField(max_length=30, default="", blank=True)
