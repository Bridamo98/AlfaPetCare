from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from apps.gestor_de_usuarios.models import Profile

class Enfermedad(models.Model):
    nombre = models.CharField(max_length = 30, blank = False, null = False)
    def __str__(self): #To string
        return self.nombre

class Color(models.Model):
    nombre = models.CharField(max_length = 30, blank = False, null = False)

class Mascota(models.Model):
    TIPOS = (
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
    )
    SEXO = (
        ('Macho', 'Macho'),
        ('Hembra', 'Hembra'),
    )
    RAZAS = (
        ('','---------'),
        ('Weimaraner', 'Weimaraner'),
        ('Viejo Pastor Inglés', 'Viejo Pastor Inglés'),
        ('Terrier Yorkshire', 'Terrier Yorkshire'),
        ('Terrier Escocés', 'Terrier Escocés'),
        ('Terranova', 'Terranova'),
        ('Springer Spaniel', 'Springer Spaniel'),
        ('Shih Tzu', 'Shih Tzu'),
        ('Shiba Inu', 'Shiba Inu'),
        ('Shar Pei', 'Shar Pei'),
        ('Schnauzer Miniatura', 'Schnauzer Miniatura'),
        ('San Bernardo', 'San Bernardo'),
        ('Rottweiler', 'Rottweiler'),
        ('Pug', 'Pug'),
        ('Poodle', 'Poodle'),
        ('Pomeranio', 'Pomeranio'),
        ('Pitbull terrier', 'Pitbull terrier'),
        ('Pinscher', 'Pinscher'),
        ('Corgi', 'Corgi'),
        ('Pekinés', 'Pekinés'),
        ('Pastor de Shetland', 'Pastor de Shetland'),
        ('Pastor Australiano', 'Pastor Australiano'),
        ('Pastor Alemán', 'Pastor Alemán'),
        ('Malamute de Alaska', 'Malamute de Alaska'),
        ('Labrador Retriever', 'Labrador Retriever'),
        ('Husky Siberiano', 'Husky Siberiano'),
        ('Gran Danés', 'Gran Danés'),
        ('Golden Retriever', 'Golden Retriever'),
        ('Galgo', 'Galgo'),
        ('Flat Coated Retriever', 'Flat Coated Retriever'),
        ('Doberman', 'Doberman'),
        ('Dálmata', 'Dálmata'),
        ('Dachshund', 'Dachshund'),
        ('Collie', 'Collie'),
        ('Cocker Spaniel', 'Cocker Spaniel'),
        ('Chow Chow', 'Chow Chow'),
        ('Chihuahua', 'Chihuahua'),
        ('Bulldog francés', 'Bulldog francés'),
        ('Bulldog', 'Bulldog'),
        ('Bóxer', 'Bóxer'),
        ('Boston Terrier', 'Boston Terrier'),
        ('Border Collie', 'Border Collie'),
        ('Basset Hound', 'Basset Hound'),
        ('Akita americano', 'Akita americano'),
        ('Criollo', 'Criollo'),

        ('Curl Americano', 'Curl Americano'),
        ('Búrmes', 'Búrmes'),
        ('Munchkin', 'Munchkin'),
        ('Devon Rex', 'Devon Rex'),
        ('Oriental', 'Oriental'),
        ('Scottish Fold', 'Scottish Fold'),
        ('Van Turco', 'Van Turco'),
        ('Korat', 'Korat'),
        ('Somalí', 'Somalí'),
        ('Sphynx', 'Sphynx'),
        ('Siberiano', 'Siberiano'),
        ('Exótico', 'Exótico'),
        ('Birmano', 'Birmano'),
        ('Bosque de Noruega', 'Bosque de Noruega'),
        ('Bengalí', 'Bengalí'),
        ('Abisinio', 'Abisinio'),
        ('Balinés', 'Balinés'),
        ('Maine Coon', 'Maine Coon'),
        ('British Shorthair', 'British Shorthair'),
        ('Ruso Azul', 'Ruso Azul'),
        ('Bombay', 'Bombay'),
        ('Persa', 'Persa'),
        ('Siamés', 'Siamés'),
        ('Ragdoll', 'Ragdoll'),
        ('Criollo', 'Criollo'),
    )
    usuario = models.ForeignKey(Profile,on_delete=models.CASCADE,null=False)
    nombre = models.CharField(max_length = 30, blank = False, null = False)
    tipo = models.CharField(max_length = 6, blank = False, null = False, choices = TIPOS)
    fecha_nacimiento = models.DateField('Fecha nacimiento', blank = False, null = False)
    sexo = models.CharField(max_length = 7, blank = False, null = False, choices = SEXO)
    raza = models.CharField(max_length = 30, blank = False, null = False, choices = RAZAS, default = None)
    color = models.ManyToManyField(Color, blank=True)
    enfermedades = models.ManyToManyField(Enfermedad, blank=True)
    #color = models.CharField(max_length = 20, blank = False, null = False)
    #peso = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(1),MaxValueValidator(100)])
    #tamanio = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(1),MaxValueValidator(100)])
