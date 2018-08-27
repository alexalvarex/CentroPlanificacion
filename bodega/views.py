from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from central.models import *
from django.db.models import Count
from django.db.models import Max


from django.contrib.auth.models import User
import datetime, time
now = datetime.datetime.now()

@login_required()
def index_bodega(request):
	if request.user.Colaborador.tipo_acceso.tipo_acceso == "Bodega":
		return render(request, 'index_bodega.html')
	else:
		return render(request, 'index.html')