from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^$', views.index_facturas, name='index'),
	url(r'resultados/$', views.resultados, name='resultados'),
	url(r'configuracion/$', views.configuracion, name='configuracion'),
	url(r'configuracion/add/$', views.configuracion_add, name='configuracion_add'),
	url(r'ordenservicio/$', views.orden_servicio, name='orden_servicio'),
	url(r'ordenservicio/all/$', views.orden_servicio_general, name='orden_servicio_general'),
	url(r'ordenservicio/actuales/$', views.orden_servicio_all, name='orden_servicio_all'),
	url(r'ordenservicio/add/$', views.orden_servicio_add, name='orden_servicio_add'),
	url(r'ordeninterna/$', views.orden_interna, name='orden_interna'),
	url(r'ordeninterna/all/$', views.orden_interna_general, name='orden_interna_general'),
	url(r'ordeninterna/actuales/$', views.orden_interna_all, name='orden_interna_all'),
	url(r'ordeninterna/add/$', views.orden_interna_add, name='orden_interna_add'),

]