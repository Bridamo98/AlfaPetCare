from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from apps.gestor_de_usuarios.models import Profile

class Enfermedad(models.Model):
    nombre = models.CharField(max_length = 30, blank = False, null = False)
    def __str__(self): #To string
        return self.nombre

class Mascota(models.Model):
    TIPOS = (
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
    )
    SEXO = (
        ('Macho', 'Macho'),
        ('Hembra', 'Hembra'),
    )
    usuario = models.ForeignKey(Profile,on_delete=models.CASCADE,null=False)
    nombre = models.CharField(max_length = 30, blank = False, null = False)
    tipo = models.CharField(max_length = 6, blank = False, null = False, choices = TIPOS)
    fecha_nacimiento = models.DateField('Fecha nacimiento', blank = False, null = False)
    sexo = models.CharField(max_length = 7, blank = False, null = False, choices = SEXO)
    enfermedades = models.ManyToManyField(Enfermedad, blank=True)
    #raza = models.CharField(max_length = 30, blank = False, null = False)
    #color = models.CharField(max_length = 20, blank = False, null = False)
    #peso = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(1),MaxValueValidator(100)])
    #tamanio = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(1),MaxValueValidator(100)])
