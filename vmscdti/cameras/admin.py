from django.contrib import admin
from .models import RolesDB, CamarasDB

# Register your models here.





class RolAdmin(admin.ModelAdmin):
    fields = ['nombre']
    list_display = ['nombre']

admin.site.register(RolesDB, RolAdmin)


class CamaraAdmin(admin.ModelAdmin):
    fields = ['nombre_usuario', 'passwords', 'ip_camara','puerto','lugar']
    list_display = ['nombre_usuario', 'passwords', 'ip_camara','puerto','lugar']

admin.site.register(CamarasDB, CamaraAdmin)