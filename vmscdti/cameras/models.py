from django.db import models

# Create your models here.

class RolesDB(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="NombreRol",null=False, blank=False)

    class Meta:
        db_table = "roles"
        verbose_name ="rol"
        verbose_name_plural ="roles"
    
    def __str__(self):
        return self.nombre



class BloquesDB(models.Model):
    nombre = models.CharField(max_length=5, verbose_name="NombreBloque", null=False, blank=False)
    class Meta:
        db_table = "bloques"
        verbose_name ="bloque"
        verbose_name_plural ="bloques"


    def __str__(self):
        return self.nombre


class AmbientesDB(models.Model):
    nombre = models.CharField(max_length=70, verbose_name="NombreAmbiente", null=False, blank=False)
    bloque_fk = models.ForeignKey(BloquesDB, on_delete=models.CASCADE)

    class Meta:
        db_table = "ambientes"
        verbose_name ="ambiente"
        verbose_name_plural ="ambientes"

    def __str__(self):
        return self.nombre



class CamarasDB(models.Model):
    nombre_usuario=models.CharField(max_length=80, verbose_name="NombreUsuario", null=False, blank=False)
    passwords = models.CharField(max_length=20, verbose_name="password", null=False, blank=False)
    ip_camara = models.GenericIPAddressField(verbose_name="IP Camara", null=False, blank=False)
    puerto=models.CharField(max_length=15, verbose_name="puerto", null=False, blank=False) 

    class Meta:
        db_table = "camaras"
        verbose_name ="camara"
        verbose_name_plural ="camaras"
        
    def __str__(self):
        return self.nombre_usuario




    
