from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

class Topico(models.Model):
    nombre = models.CharField(max_length = 30, blank = False, null = False)
    def __str__(self): #To string
        return self.nombre

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tfno = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(1000000),MaxValueValidator(9999999999)])
    topicos = models.ManyToManyField(Topico, blank=True)
    foto = models.ImageField(upload_to='images/',default = 'images/anonimo.png', null = True, blank = True)
    #profile_img=models.ImageField(upload_to='images/profile/',default='images/profile/perfilb.jpg',null=False,blank=False)
    def __str__(self): #To string
        return self.user.username

class Servicio(models.Model):
    TIPOS = (
        ('Adopción', 'Adopción'),
        ('Esterilización', 'Esterilización'),
        ('Vacunación', 'Vacunación'),
        ('Feria de mascotas', 'Feria de mascotas'),
    )
    usuario = models.OneToOneField(Profile, on_delete=models.CASCADE)

    nombre_responsable = models.CharField(max_length = 100, blank = False, null = False)
    correo = models.EmailField(default = "Ninguno",null = True,blank=True)
    telefono = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(1000000),MaxValueValidator(9999999999)])
    logo = models.ImageField(upload_to='logos/',default = 'images/servicio.png', null = True, blank = True)

    direccion = models.CharField(max_length = 256, blank = False, null = False)
    longitud = models.FloatField(null=True, blank=True, default=None)#------
    latitud = models.FloatField(null=True, blank=True, default=None)#------

    #profile_img=models.ImageField(upload_to='images/profile/',default='images/profile/perfilb.jpg',null=False,blank=False)
    def __str__(self): #To string
        return self.user.user
