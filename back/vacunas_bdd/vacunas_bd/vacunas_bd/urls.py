from django.contrib import admin
from django.urls import path,include
from vacunas_bd.datos_bd import index, eliminar, registrar

urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('', index, name='home'), 
    path('index', index, name='index'),
    path('app_gestion/', include('api.urls')), 
    path('eliminar/<rut>', eliminar, name='eliminar'), 
   path('registrar', registrar, name='registrar'),
]



