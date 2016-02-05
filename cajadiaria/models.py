from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class CajaDiaria(models.Model):
	saldoinicial = models.FloatField(default='00.00')
	saldofinal = models.FloatField(default='00.00')
	fecha = models.DateTimeField(auto_now=True)
	usuario = models.ForeignKey(User)

		
