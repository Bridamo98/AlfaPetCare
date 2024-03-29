from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
"""
Representa un topico dentro del sistema
Atributos:
-nombre: nombre de topico
"""
class Topico(models.Model):
    nombre = models.CharField(max_length = 30, blank = False, null = False)
    def __str__(self): #To string
        return self.nombre
"""
Representa un perfil dentro del sistema
Atributos:
-user = usuario asociado al perfil
-tfno = telefono del perfil
-topicos = conjunto de topicos asociados al perfil
-foto = foto del perfil
"""
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tfno = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(1000000),MaxValueValidator(9999999999)])
    topicos = models.ManyToManyField(Topico, blank=True)
    foto = models.ImageField(upload_to='images/',default = 'images/anonimo.png', null = True, blank = True)
    #profile_img=models.ImageField(upload_to='images/profile/',default='images/profile/perfilb.jpg',null=False,blank=False)
    def __str__(self): #To string
        return self.user.username
"""
Representa un servicio dentro del sistema
Atributos:
-usuario = usuario asociado al servicio
-tipo = tipo del servicio
-direccion = dirección del lugar de atención donde se presta el servicio
-longitud = longitud de la posición
-latitud = latitud de la posición
-calificacion = calificación del servicio
-cantidad_calif = cantidad de calificaciones realizadas
"""
class Servicio(models.Model):
    TIPOS = (
        ('Guardería', 'Guardería'),
        ('Niñera', 'Niñera'),
        ('Rescatista', 'Rescatista'),
        ('Refugio', 'Refugio'),
        ('Hogar de paso', 'Hogar de paso'),
        ('Centro de Adopción', 'Centro de Adopción'),
        ('Paseador', 'Paseador'),
        ('Servicio de Transporte', 'Servicio de Transporte'),
        ('Servicio Funerario', 'Servicio Funerario'),
        ('Fundación de ayuda', 'Fundación de ayuda'),
    )
    usuario = models.ForeignKey(Profile, on_delete=models.CASCADE)

    tipo = models.CharField(max_length = 100, blank = False, null = False, choices = TIPOS, default=None)

    direccion = models.CharField(max_length = 256, blank = False, null = False, default=None)
    longitud = models.FloatField(null=True, blank=True, default=None)#------
    latitud = models.FloatField(null=True, blank=True, default=None)#------

    calificacion = models.FloatField(null=True, blank=True, default=None, validators=[MinValueValidator(0.0),MaxValueValidator(5.0)])#------
    cantidad_calif = models.PositiveIntegerField(blank=True, null=True, default = 0)

    #profile_img=models.ImageField(upload_to='images/profile/',default='images/profile/perfilb.jpg',null=False,blank=False)
    def __str__(self): #To string
        return self.tipo
