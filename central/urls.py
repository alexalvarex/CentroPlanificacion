from django.conf.urls import (url, handler400, handler403, handler404, handler500 )
from . import views
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^usuarios/$', views.usuarios, name='usuarios'),
	url(r'^usuarios/delete/(?P<pk>\d+)/$', views.usuarios_delete, name='usuarios_delete'),
	url(r'^usuarios/add/$', views.usuarios_add, name='usuarios_add'),

]