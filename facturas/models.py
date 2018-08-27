from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.utils import timezone

class Familia(models.Model):
	familia = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=100)

	def __unicode__(self):
		return str(self.familia) + " " + str(self.id)

@python_2_unicode_compatible
class Categoria(models.Model):
	categoria = models.CharField(max_length=100)
	familia = models.ForeignKey(Familia)

	def __str__(self):
		return self.categoria

class Equipo(models.Model):
	codigo = models.IntegerField()
	descripcion = models.CharField(max_length=100)
	categoria = models.ForeignKey(Categoria)
	ceco = models.CharField(max_length=100, blank=True, null=True)

	def __unicode__(self):
		return str(self.codigo)

@python_2_unicode_compatible
class Proveedor(models.Model):
	codigo = models.IntegerField(blank=True, null=True)
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre

@python_2_unicode_compatible
class MAG(models.Model):
	motivo = models.CharField(max_length=100)

	def __str__(self):
		return self.motivo

@python_2_unicode_compatible
class TipoOrden(models.Model):
	tipo_orden = models.CharField(max_length=100)

	def __str__(self):
		return self.tipo_orden

@python_2_unicode_compatible
class Mes(models.Model):
	mes = models.CharField(max_length=100)

	def __str__(self):
		return self.mes

@python_2_unicode_compatible
class Configuracion(models.Model):
	mes = models.ForeignKey(Mes)
	fecha_inicial = models.DateField()
	fecha_final = models.DateField()

	def __str__(self):
		return str(self.mes)

@python_2_unicode_compatible
class Orden(models.Model):
	orden_trabajo = models.CharField(max_length=100, blank=True, null=True)
	solped = models.CharField(max_length=100, blank=True, null=True)
	orden_servico = models.CharField(max_length=100)
	proveedor = models.ForeignKey(Proveedor)
	num_factura = models.IntegerField()
	mag = models.ForeignKey(MAG)
	equipo = models.ForeignKey(Equipo)
	monto_lps = models.FloatField()
	descripcion = models.CharField(max_length=100)
	fecha_fac = models.DateField()
	fecha_reg = models.DateField()
	fecha_pago = models.DateField()
	tipo_orden = models.ForeignKey(TipoOrden)
	confiactual = models.ForeignKey(Configuracion)

	def __str__(self):
		return self.orden_servico + " " + str(self.equipo) + 'Mes: ' + str(self.confiactual.mes)