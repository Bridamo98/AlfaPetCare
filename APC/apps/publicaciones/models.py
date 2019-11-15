from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from apps.gestor_de_usuarios.models import Profile, Topico
from django.utils import timezone


class Lugar(models.Model):
    TIPOS = (
        ('Clínicas veterinarias','Clínicas veterinarias'),
        ('Consultorios veterinarios','Consultorios veterinarios'),
        ('Refugios','Refugios'),
        ('Centros de adopción','Centros de adopción'),
        ('Fundaciones','Fundaciones'),
        ('Guarderías','Guarderias'),
        ('Sitio Pet Friendly','Sitio Pet Friendly'),
        ('Tiendas para mascotas','Tiendas para mascotas'),
        ('Spa para mascotas','Spa para mascotas'),
        ('Eventos','Eventos'),
        ('Zona dee peligro','Zona de peligro'),
    )
    nombre_lugar = models.CharField(max_length = 30, blank = False, null = False)
    tipo_lugar = models.CharField(max_length = 10, blank = False, null = False, choices = TIPOS)
    telefono_cel = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(1000000),MaxValueValidator(9999999999)])
    email = models.EmailField(max_length = 256, blank = False, null = False)
    direccion = models.CharField(max_length = 10, blank = False, null = False)
    def __str__(self): #To string
        return self.nombre_lugar



class Evento_global(models.Model):
    TIPOS = (
        ('Global', 'Global'),
        ('Personal', 'Personal'),
    )
    usuario = models.ForeignKey(Profile,on_delete=models.CASCADE,null=False)
    nombre_evento = models.CharField(max_length = 30, blank = False, null = False)
    tipo_evento = models.CharField(max_length = 10, blank = False, null = False, choices = TIPOS)
    fecha_evento = models.DateField('Fecha del evento', blank = False, null = False)
    hora_evento = models.DateTimeField(auto_now=False, auto_now_add=False)
    lugar = models.ForeignKey(Lugar,on_delete=models.CASCADE,null=False)


    def __str__(self): #To string
        return self.nombre_evento

class Conversacion_global(models.Model):
    usuario = models.ForeignKey(Profile,on_delete=models.CASCADE,null=False)
    titulo = models.CharField(max_length = 100, blank = False, null = False)
    topico = models.ForeignKey(Topico,on_delete=models.CASCADE,null=False)

    def __str__(self): #To string
        return self.titulo

class Mensaje(models.Model):
    usuario = models.ForeignKey(Profile,on_delete=models.CASCADE,null=False)
    contenido = models.TextField(blank = False, null = False)
    fecha = models.DateTimeField(default=timezone.now)
    conversacion = models.ForeignKey(Conversacion_global, on_delete=models.CASCADE, null = False)

    def __str__(self): #To string
        return self.contenido
