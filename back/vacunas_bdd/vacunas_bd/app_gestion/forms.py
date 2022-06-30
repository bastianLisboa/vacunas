from django import forms 
from app_gestion.models import Datos_vacuna 

class Datos_vacuna_Form (forms.Datos_vacuna_Form ): 
    class Meta: 
        model = Datos_vacuna 
        fields = ['rut', 'nombre', 'apellido_mat', 'apellido_pat', 'edad', 'vacuna','tipo_vacuna', 'fecha'] 