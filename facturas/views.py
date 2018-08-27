from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import *
from django.db.models import Count, Sum
from django.db.models import Max


from django.contrib.auth.models import User
import datetime, time
now = datetime.datetime.now()

@login_required()
def index_facturas(request):
	if request.user.Colaborador.tipo_acceso.tipo_acceso == "Facturacion":
		return render(request, 'index_facturas.html')
	else:
		return render(request, 'index.html')

@login_required()
def orden_servicio(request):
	if request.user.Colaborador.tipo_acceso.tipo_acceso == "Facturacion":
		proveedores = Proveedor.objects.all()
		mag = MAG.objects.all()
		equipos = Equipo.objects.all()
		confiactual = Configuracion.objects.latest('id')
		to = TipoOrden.objects.get(pk=2)
		cantorg = Orden.objects.filter(tipo_orden = to)
		cantor = Orden.objects.filter(tipo_orden = to).filter(confiactual = confiactual)
		cantors = cantor.count()
		cantorsg = cantorg.count()
		hoy = now
		dias = confiactual.fecha_final.day - now.day
		return render(request, 'orden_servicio.html', {'proveedores':proveedores, 'mag':mag,
			'equipos':equipos, 'cantors':cantors, 'confiactual':confiactual, 'dias':dias, 'hoy':hoy,
			'cantorsg':cantorsg})
	else:
		return render(request, 'index.html')


@login_required()
def orden_servicio_general(request):
	if request.user.Colaborador.tipo_acceso.tipo_acceso == "Facturacion":
		cantor = Orden.objects.all()
		to = TipoOrden.objects.get(pk=2)
		ordenes = Orden.objects.filter(tipo_orden = to)
		cantors = cantor.count()

		return render(request, 'orden_servicio_general.html', {'cantors':cantors, 'ordenes': ordenes})
	else:
		return render(request, 'index.html')

@login_required()
def orden_servicio_all(request):
	if request.user.Colaborador.tipo_acceso.tipo_acceso == "Facturacion":
		proveedores = Proveedor.objects.all()
		mag = MAG.objects.all()
		equipos = Equipo.objects.all()
		confiactual = Configuracion.objects.latest('id')
		to = TipoOrden.objects.get(pk=2)
		cantor = Orden.objects.filter(tipo_orden = to).filter(confiactual = confiactual)
		ordenes = Orden.objects.filter(tipo_orden = to).filter(confiactual = confiactual)
		cantors = cantor.count()

		dias = confiactual.fecha_final.day - now.day
		return render(request, 'ordenes_servicio.html', {'proveedores':proveedores, 'mag':mag,
			'equipos':equipos, 'cantors':cantors, 'confiactual':confiactual, 'dias':dias, 'ordenes': ordenes})
	else:
		return render(request, 'index.html')

@login_required()
def orden_servicio_add(request):
	if request.user.Colaborador.tipo_acceso.tipo_acceso == "Facturacion":
		if request.method == 'POST':
			try:
				ordentrabajo = request.POST.get('ordentrabajo')
				solped = request.POST.get('solped')
				zona = request.POST.get('zona')
				ordenservicio = request.POST.get('ordenservicio')
				descripcion = request.POST.get('descripcion')
				nombreprove = request.POST.get('nombreprove')
				numfactura = request.POST.get('numfactura')
				mag = request.POST.get('mag')
				equipo = request.POST.get('equipo')
				monto_lps = request.POST.get('lps')
				fechafac = request.POST.get('fechafac')
				fechareg = request.POST.get('fechareg')
				fechapago = request.POST.get('fechapago')

				provee = Proveedor.objects.get(pk = nombreprove)
				motivo = MAG.objects.get(pk = mag)
				equip = Equipo.objects.get(pk = equipo)
				tipo_orden = TipoOrden.objects.get(pk = 2)
				confiactual = Configuracion.objects.latest('id')

				orden = Orden(
						orden_trabajo = ordentrabajo,
						solped = solped,
						orden_servico = ordenservicio,
						proveedor = provee,
						num_factura = numfactura,
						mag = motivo,
						equipo = equip,
						monto_lps = monto_lps,
						descripcion = descripcion,
						fecha_fac = fechafac,
						fecha_reg = fechareg,
						fecha_pago = fechapago,
						tipo_orden = tipo_orden,
						confiactual = confiactual)
				orden.save()
				return HttpResponseRedirect(reverse('orden_servicio'))
			except Exception as e:
				return HttpResponse(e)
	else:
		return render(request, 'index.html')

@login_required()
def orden_interna(request):
	if request.user.Colaborador.tipo_acceso.tipo_acceso == "Facturacion":
		proveedores = Proveedor.objects.all()
		mag = MAG.objects.all()
		equipos = Equipo.objects.all()
		confiactual = Configuracion.objects.latest('id')
		to = TipoOrden.objects.get(pk=1)
		cantorg = Orden.objects.filter(tipo_orden = to)
		cantor = Orden.objects.filter(tipo_orden = to).filter(confiactual = confiactual)
		cantors = cantor.count()
		cantorsg = cantorg.count()

		dias = confiactual.fecha_final.day - now.day
		return render(request, 'orden_interna.html', {'proveedores':proveedores, 'mag':mag,
			'equipos':equipos, 'cantors':cantors, 'confiactual':confiactual, 'dias':dias, 'cantorsg':cantorsg})
	else:
		return render(request, 'index.html')

@login_required()
def orden_interna_general(request):
	if request.user.Colaborador.tipo_acceso.tipo_acceso == "Facturacion":
		to = TipoOrden.objects.get(pk=1)
		ordenes = Orden.objects.filter(tipo_orden = to)
		cantors = ordenes.count()

		return render(request, 'orden_interna_general.html', {'ordenes': ordenes, 'cantors':cantors})
	else:
		return render(request, 'index.html')

@login_required()
def orden_interna_all(request):
	if request.user.Colaborador.tipo_acceso.tipo_acceso == "Facturacion":
		proveedores = Proveedor.objects.all()
		mag = MAG.objects.all()
		equipos = Equipo.objects.all()
		confiactual = Configuracion.objects.latest('id')
		to = TipoOrden.objects.get(pk=1)
		cantor = Orden.objects.filter(tipo_orden = to).filter(confiactual = confiactual)
		cantors = cantor.count()
		tipo_orden = TipoOrden.objects.get(pk = 1)
		ordenes = Orden.objects.filter(tipo_orden = tipo_orden).filter(confiactual = confiactual)

		dias = confiactual.fecha_final.day - now.day
		return render(request, 'ordenes_interna.html', {'proveedores':proveedores, 'mag':mag,
			'equipos':equipos, 'cantors':cantors, 'confiactual':confiactual, 'dias':dias, 'ordenes': ordenes})
	else:
		return render(request, 'index.html')

@login_required()
def orden_interna_add(request):
	if request.user.Colaborador.tipo_acceso.tipo_acceso == "Facturacion":
		if request.method == 'POST':
			try:
				ordentrabajo = request.POST.get('ordentrabajo')
				solped = request.POST.get('solped')
				zona = request.POST.get('zona')
				ordenservicio = request.POST.get('ordenservicio')
				descripcion = request.POST.get('descripcion')
				nombreprove = request.POST.get('nombreprove')
				numfactura = request.POST.get('numfactura')
				mag = request.POST.get('mag')
				equipo = request.POST.get('equipo')
				monto_lps = request.POST.get('lps')
				fechafac = request.POST.get('fechafac')
				fechareg = request.POST.get('fechareg')
				fechapago = request.POST.get('fechapago')

				provee = Proveedor.objects.get(pk = nombreprove)
				motivo = MAG.objects.get(pk = mag)
				equip = Equipo.objects.get(pk = equipo)
				tipo_orden = TipoOrden.objects.get(pk = 1)
				confiactual = Configuracion.objects.latest('id')

				orden = Orden(
						orden_trabajo = ordentrabajo,
						solped = solped,
						orden_servico = ordenservicio,
						proveedor = provee,
						num_factura = numfactura,
						mag = motivo,
						equipo = equip,
						monto_lps = monto_lps,
						descripcion = descripcion,
						fecha_fac = fechafac,
						fecha_reg = fechareg,
						fecha_pago = fechapago,
						tipo_orden = tipo_orden,
						confiactual = confiactual)
				orden.save()
				return HttpResponseRedirect(reverse('orden_interna'))
			except Exception as e:
				return HttpResponse(e)
	else:
		return render(request, 'index.html')

@login_required()
def configuracion(request):
	if request.user.Colaborador.tipo_acceso.tipo_acceso == "Facturacion":
		confiactual = Configuracion.objects.latest('id')
		mes = Mes.objects.all()

		return render(request, 'configuracion.html', {'confiactual': confiactual, 'mes':mes})
	else:
		return render(request, 'index.html')

@login_required()
def configuracion_add(request):
	if request.user.Colaborador.tipo_acceso.tipo_acceso == "Facturacion":
		if request.method == 'POST':
			try:
				mes = request.POST.get('mes')
				fechai = request.POST.get('fechai')
				fecham = request.POST.get('fecham')
				
				mesac = Mes.objects.get(pk = mes)

				confi = Configuracion(
						mes = mesac,
						fecha_inicial = fechai,
						fecha_final = fecham)
				confi.save()
				return HttpResponseRedirect(reverse('configuracion'))
			except Exception as e:
				return HttpResponse(e)
	else:
		return render(request, 'index.html')


@login_required()
def resultados(request):
	if request.user.Colaborador.tipo_acceso.tipo_acceso == "Facturacion":

		# ACTUALES
		confiactual = Configuracion.objects.latest('id')
		mes = Mes.objects.all()
		# ORDENES
		os = TipoOrden.objects.get(pk = 2)
		oi = TipoOrden.objects.get(pk = 1)
		ordenservicio = Orden.objects.filter(tipo_orden = os).filter(confiactual = confiactual)
		ordeninterna = Orden.objects.filter(tipo_orden = oi).filter(confiactual = confiactual)
		cantos = ordenservicio.count()
		cantoi = ordeninterna.count()

		# FAMILIAS
		fm501 = Familia.objects.get(pk = 1)
		fm502 = Familia.objects.get(pk = 2)
		fm503 = Familia.objects.get(pk = 3)
		fm504 = Familia.objects.get(pk = 4)
		fm505 = Familia.objects.get(pk = 5)
		fm506 = Familia.objects.get(pk = 6)
		fm507 = Familia.objects.get(pk = 7)
		fm508 = Familia.objects.get(pk = 8)
		fm508 = Familia.objects.get(pk = 8)
		fm509 = Familia.objects.get(pk = 9)
		fm509 = Familia.objects.get(pk = 9)
		fm510 = Familia.objects.get(pk =10)
		fm511 = Familia.objects.get(pk =11)
		fm512 = Familia.objects.get(pk =12)
		fm513 = Familia.objects.get(pk =13)
		fm508TS = Familia.objects.get(pk =14)

		cant501 = Orden.objects.filter(equipo__categoria__familia = fm501).filter(confiactual = confiactual).count()
		cant502 = Orden.objects.filter(equipo__categoria__familia = fm502).filter(confiactual = confiactual).count()
		cant503 = Orden.objects.filter(equipo__categoria__familia = fm503).filter(confiactual = confiactual).count()
		cant504 = Orden.objects.filter(equipo__categoria__familia = fm504).filter(confiactual = confiactual).count()
		cant505 = Orden.objects.filter(equipo__categoria__familia = fm505).filter(confiactual = confiactual).count()
		cant506 = Orden.objects.filter(equipo__categoria__familia = fm506).filter(confiactual = confiactual).count()
		cant507 = Orden.objects.filter(equipo__categoria__familia = fm507).filter(confiactual = confiactual).count()
		cant508 = Orden.objects.filter(equipo__categoria__familia = fm508).filter(confiactual = confiactual).count()
		cant509 = Orden.objects.filter(equipo__categoria__familia = fm509).filter(confiactual = confiactual).count()
		cant510 = Orden.objects.filter(equipo__categoria__familia = fm510).filter(confiactual = confiactual).count()
		cant511 = Orden.objects.filter(equipo__categoria__familia = fm511).filter(confiactual = confiactual).count()
		cant512 = Orden.objects.filter(equipo__categoria__familia = fm512).filter(confiactual = confiactual).count()
		cant513 = Orden.objects.filter(equipo__categoria__familia = fm513).filter(confiactual = confiactual).count()
		cant508TS = Orden.objects.filter(equipo__categoria__familia = fm508TS).filter(confiactual = confiactual).count()


		# PROVEEDORES
		proveedores = Proveedor.objects.all()
		# provemax = Orden.objects.values('proveedor').annotate(cant_prov = Count('proveedor')).group_by('proveedor')[:5]
		provemax = Orden.objects.values('proveedor').filter(confiactual = confiactual).annotate(cant_prov = Count('proveedor'))[:3]
		provemont = Orden.objects.values('proveedor').filter(confiactual = confiactual).annotate(monto_prov = Sum('monto_lps'))[:3]

		# GASTOS
		malaop = Orden.objects.filter(mag = 1).filter(confiactual = confiactual).count()
		accidente = Orden.objects.filter(mag = 2).filter(confiactual = confiactual).count()
		gasto = Orden.objects.filter(mag = 3).filter(confiactual = confiactual).count()

		# GENERALES
		# ORDENES
		os = TipoOrden.objects.get(pk = 2)
		oi = TipoOrden.objects.get(pk = 1)
		ordenservicio = Orden.objects.filter(tipo_orden = os)
		ordeninterna = Orden.objects.filter(tipo_orden = oi)
		cantos1 = ordenservicio.count()
		cantoi1 = ordeninterna.count()

		# FAMILIAS
		cant5011 = Orden.objects.filter(equipo__categoria__familia = fm501).count()
		cant5021 = Orden.objects.filter(equipo__categoria__familia = fm502).count()
		cant5031 = Orden.objects.filter(equipo__categoria__familia = fm503).count()
		cant5041 = Orden.objects.filter(equipo__categoria__familia = fm504).count()
		cant5051 = Orden.objects.filter(equipo__categoria__familia = fm505).count()
		cant5061 = Orden.objects.filter(equipo__categoria__familia = fm506).count()
		cant5071 = Orden.objects.filter(equipo__categoria__familia = fm507).count()
		cant5081 = Orden.objects.filter(equipo__categoria__familia = fm508).count()
		cant5091 = Orden.objects.filter(equipo__categoria__familia = fm509).count()
		cant5101 = Orden.objects.filter(equipo__categoria__familia = fm510).count()
		cant5111 = Orden.objects.filter(equipo__categoria__familia = fm511).count()
		cant5121 = Orden.objects.filter(equipo__categoria__familia = fm512).count()
		cant5131 = Orden.objects.filter(equipo__categoria__familia = fm513).count()
		cant508TS1 = Orden.objects.filter(equipo__categoria__familia = fm508TS).count()

		# PROVEEDORES
		provemax1 = Orden.objects.values('proveedor').annotate(cant_prov = Count('proveedor'))[:3]
		provemont1 = Orden.objects.values('proveedor').annotate(monto_prov = Sum('monto_lps'))[:3]

		# GASTOS
		malaop1 = Orden.objects.filter(mag = 1).count()
		accidente1 = Orden.objects.filter(mag = 2).count()
		gasto1 = Orden.objects.filter(mag = 3).count()


		return render(request, 'resultados.html', {'confiactual':confiactual,'cantos':cantos, 
			'cantoi':cantoi, 'cant501':cant501,'cant502':cant502,'cant503':cant503,'cant504':cant504,
			'cant505':cant505,'cant506':cant506,'cant507':cant507,'cant508':cant508,'cant509':cant509,
			'cant510':cant510,'cant511':cant511,'cant512':cant512,'cant513':cant513,'cant508TS':cant508TS,
			'provemax':provemax, 'provemont':provemont, 'proveedores':proveedores,
			'malaop':malaop, 'accidente':accidente,'gasto':gasto,
			'cantos1':cantos1, 'cantoi1':cantoi1, 'cant5011':cant5011,'cant5021':cant5021,'cant5031':cant5031,
			'cant5041':cant5041, 'cant5051':cant5051,'cant5061':cant5061,'cant5071':cant5071,'cant5081':cant5081,
			'cant5091':cant5091, 'cant5101':cant5101,'cant5111':cant5111,'cant5121':cant5121,'cant5131':cant5131,
			'cant508TS1':cant508TS1,
			'provemax1':provemax1, 'provemont1':provemont1,
			'malaop1':malaop1, 'accidente1':accidente1,'gasto1':gasto1})
	else:
		return render(request, 'index.html')