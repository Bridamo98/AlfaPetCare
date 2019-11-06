from django.urls import path
from .views import registro_mascota
urlpatterns = [
    path('registrar_mascota/',registro_mascota, name = 'registrar_mascota')
]
