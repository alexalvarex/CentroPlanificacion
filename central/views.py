from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import *
from django.db.models import Count
from django.db.models import Max


from django.contrib.auth.models import User
import datetime, time
now = datetime.datetime.now()

@login_required()
def index(request):
	return render(request, 'index.html')

@login_required()
def usuarios(request):
	colaboradores = Colaborador.objects.all()
	usuarios = User.objects.all()
	numu = colaboradores.count()
	accesos = Acceso.objects.all()
	return render(request, 'usuarios.html', {'colaboradores': colaboradores, 'usuarios':usuarios, 'numu':numu,
		'accesos':accesos})


@login_required()
def usuarios_delete(request, pk):
	if request.user.is_staff:
		colaborador = Colaborador.objects.get(pk = pk)
		try:
			colaborador.delete()
			return HttpResponseRedirect(reverse('usuarios'))
		except Exception, e:
			return HttpResponse(e)
	else:
		return render(request, '404.html')


@login_required()
def usuarios_add(request):
		if request.method == 'POST':
			try:
				username = request.POST.get('username')
				password = request.POST.get('contra')
				first_name = request.POST.get('first_name')
				last_name = request.POST.get('last_name')
				correo = request.POST.get('correo')
				accesos = request.POST.getlist('acceso[]')

				usuario = User.objects.create(
						username = username, 
						password = password, 
						first_name = first_name, 
						last_name = last_name,
						email = correo
						)

				colaborador = Colaborador(
						usuario = usuario,
					)
				colaborador.save()

				for acceso in accesos:
					ac = Acceso.objects.get(pk = acceso)
					colaborador.tipo_acceso.add(ac)
				return HttpResponseRedirect(reverse('usuarios'))
			except Exception as e:
				return HttpResponse(e)