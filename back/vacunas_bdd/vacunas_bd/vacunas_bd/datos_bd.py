import re  #importar libreria re
from tkinter import EW #importar libreria tkinter
from django.shortcuts import redirect, render 
from app_gestion.models import Datos_vacuna 
from app_gestion.forms import Datos_vacuna_Form 


def index(request):
    Datos_vacunas = Datos_vacuna.objects.all()
    return render(request, '/front/Informacion/informacion.html', {'Datos_vacuna': Datos_vacunas}) 


def eliminar(request, rut):
    remover = Datos_vacuna.objects.get(rut=rut) 
    remover.delete() 
    return redirect('informacion')


def registrar(request): 
    rut = request.POST.get('rut') 
    nombre = request.POST.get('nombre')
    apellido_mat = request.POST.get('apellido_mat') 
    apellido_pat = request.POST.get('apellido_pat') 
    edad = request.POST.get('edad') 
    vacuna = request.POST.get('vacuna') 
    tipo_vacuna = request.POST.get('Tipo_Vacuna') 
    fecha = request.POST.get('fecha') 
    registro=Datos_vacuna.objects.create(rut=rut, nombre=nombre, apellido_mat=apellido_mat, apellido_pat=apellido_pat, edad=edad, vacuna=vacuna, fecha=fecha) 
    return redirect('informacion') 