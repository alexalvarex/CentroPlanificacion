from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Familia)
class FamiliaAdmin(ImportExportModelAdmin):
    pass

@admin.register(Categoria)
class CategoriaAdmin(ImportExportModelAdmin):
    pass

@admin.register(Equipo)
class EquipoAdmin(ImportExportModelAdmin):
    pass


@admin.register(MAG)
@admin.register(TipoOrden)
@admin.register(Mes)
@admin.register(Configuracion)

@admin.register(Proveedor)
class ProveedorAdmin(ImportExportModelAdmin):
    pass

@admin.register(Orden)
class OrdenAdmin(ImportExportModelAdmin):
    pass