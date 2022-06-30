from django.db import models

class Datos_vacuna(models.Model): 
    rut = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=15, verbose_name='Nombre') 
    apellido_materno = models.CharField(max_length=15 , verbose_name='Apellido Materno')
    apellido_paterno = models.CharField(max_length=15, verbose_name='Apellido Materno')
    edad = models.IntegerField() 
    vacuna = models.CharField(max_length=20 , verbose_name='Nombre Vacuna') 
    tipo_vacuna = models.CharField(max_length=20 , verbose_name='Tipo Vacuna') 
    fecha = models.DateField()
