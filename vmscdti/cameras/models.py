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
    



class SectorDB(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="NombreSector",null=False, blank=False)
    

    class Meta:
        db_table = "sectores"
        verbose_name ="sector"
        verbose_name_plural ="sectores"
    
    def __str__(self):
        return self.nombre
    





class CamarasDB(models.Model):
    nombre_usuario=models.CharField(max_length=80, verbose_name="NombreUsuario", null=False, blank=False)
    passwords = models.CharField(max_length=20, verbose_name="password", null=False, blank=False)
    ip_camara = models.GenericIPAddressField(verbose_name="IP Camara", null=False, blank=False)
    puerto=models.CharField(max_length=15, verbose_name="puerto", null=False, blank=False)
    lugar=models.CharField(max_length=80, verbose_name="lugar", null=False, blank=False)
    sector_fk = models.ForeignKey(SectorDB, on_delete=models.CASCADE)

    

    class Meta:
        db_table = "camaras"
        verbose_name ="camara"
        verbose_name_plural ="camaras"
        
    def __str__(self):
        return self.nombre_usuario




    
