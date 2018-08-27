from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.utils import timezone


@python_2_unicode_compatible
class Acceso(models.Model):
	tipo_acceso = models.CharField(max_length=100)

	def __str__(self):
		return self.tipo_acceso


@python_2_unicode_compatible
class Colaborador(models.Model):
	usuario = models.OneToOneField(User, related_name='Colaborador')
	tipo_acceso = models.OneToOneField(Acceso)

	def __str__(self):
		return self.usuario.username