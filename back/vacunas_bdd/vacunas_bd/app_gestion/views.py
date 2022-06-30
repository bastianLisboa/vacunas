from django.shortcuts import render
from email import message 
from django.views import View 
from .models import Datos_vacuna
# Create your views here.
class Datos_vacuna_Views(View):
    def get(self, request):
        return render(request, '/front/Informacion/informacion.html') 

    def post(self, request):    
        return render(request, '/front/Informacion/informacion.html') 
    
    def put(self, request): 
        return render(request, '/front/Informacion/informacion.html') 

    def delete(self, request): 
        return render(request, '/front/Informacion/informacion.html') 







