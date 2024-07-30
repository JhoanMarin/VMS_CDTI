from django.contrib import admin
from .models import BloquesDB,AmbientesDB, RolesDB, CamarasDB

# Register your models here.


class BloquesAdmin(admin.ModelAdmin):
    fields = ['nombre']
    list_display = ['nombre']


admin.site.register(BloquesDB, BloquesAdmin)


class AmbienteAdmin(admin.ModelAdmin):
    fields = ['nombre', 'bloque_fk']
    list_display = ['nombre', 'bloque_fk']

admin.site.register(AmbientesDB, AmbienteAdmin)


class RolAdmin(admin.ModelAdmin):
    fields = ['nombre']
    list_display = ['nombre']

admin.site.register(RolesDB, RolAdmin)


class CamaraAdmin(admin.ModelAdmin):
    fields = ['nombre_usuario', 'passwords', 'ip_camara','puerto']
    list_display = ['nombre_usuario', 'passwords', 'ip_camara','puerto']

admin.site.register(CamarasDB, CamaraAdmin)