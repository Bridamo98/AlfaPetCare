from django.urls import path
from .views import registro_mascota, mis_mascotas

urlpatterns = [
    path('registrar_mascota/',registro_mascota, name = 'registrar_mascota'),
    path('mis_mascotas/',mis_mascotas, name = 'mis_mascotas')
]
