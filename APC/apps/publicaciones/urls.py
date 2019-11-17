from django.urls import path
from .views import *
urlpatterns = [
    path('agregar_evento_global/',agregar_evento_global, name = 'agregar_evento_global'),
    path('agregar_evento_personal/<mascota_id>/',agregar_evento_personal, name = 'agregar_evento_personal'),
    path('crear_conversacion_global/',crear_conversacion_global, name = 'crear_conversacion_global'),
    path('conversaciones_globales/',conversaciones_globales, name = 'conversaciones_globales'),
    path('ver_conversacion/<conversacion_id>/',ver_conversacion, name = 'ver_conversacion'),
    path('catalogo/buscar_conversacion_global',Conversaciones_ListView.as_view(), name = 'buscar_conversacion_global')
]
