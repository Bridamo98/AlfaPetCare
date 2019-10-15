from django.contrib import admin
from .models import Autor, Libro#Para visualizarlo en ADMIN

admin.site.register(Autor)#Para visualizarlo en ADMIN por cada clase del modelo
admin.site.register(Libro)
# Register your models here.
