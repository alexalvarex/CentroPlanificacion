from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url, include

from account.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='form_login'),
    url(r'^account/', include('account.urls')),
    url(r'^cp/', include('central.urls')),
    url(r'^bodega/', include('bodega.urls')),
    url(r'^facturas/', include('facturas.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
