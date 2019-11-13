from django.urls import path
from .views import agregar_evento_global
urlpatterns = [
    path('agregar_evento_global/',agregar_evento_global, name = 'agregar_evento_global')
]
