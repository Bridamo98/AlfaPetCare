from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from apps.gestor_de_usuarios.models import Profile
from django.core.exceptions import ValidationError
from datetime import date


"""
Entradas: value, fecha
proceso: valida si una fecha es posterior a la de hoy, en tal caso lanza una excepción
Salidas: excepción
"""
def validate_current_century(value):
    if value >= date.today():
        raise ValidationError(u'%s es una fecha inválida!' % value)
"""
Representa una enfermedad, correspondiente a una enfermedad de perros
Atributos:
-nombre: nombre de la enfermedad
"""
class Enfermedad(models.Model):
    nombre = models.CharField(max_length = 30, blank = False, null = False)
    def __str__(self): #To string
        return self.nombre

    class Meta:
        verbose_name = 'Enfermedad'
        verbose_name_plural = 'Enfermedades'
        ordering = ['nombre']
"""
Representa una enfermedad, correspondiente a una enfermedad de gatos
Atributos:
-nombre: nombre de la enfermedad
"""
class Enfermedad2(models.Model):
    nombre = models.CharField(max_length = 30, blank = False, null = False)
    def __str__(self): #To string
        return self.nombre

    class Meta:
        verbose_name = 'Enfermedad2'
        verbose_name_plural = 'Enfermedades2'
        ordering = ['nombre']
"""
Representa una mascota, que corresponde a un usuarios
Atributos:
-usuario = usuario dueño de la mascota
-nombre = nombre de la mascota
-tipo = tipo de la mascota
-fecha_nacimiento = fecha de naciemiento de la mascota
-sexo = sexo de la mascota
-raza = raza de la mascota
-color = color de la mascota
-peso = peso de la mascota
-tamanio = tamaño de la mascota
-enfermedades = conjunto de enfermedades de la mascota para perros
-enfermedades_gato = conjunto de enfermedades de la mascota para gatos
-esterilizado = indica si la mascota está esterilizada o no
-estado = estado actual de la mascota
-foto = foto de la mascota
"""
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
    TAMANIO = (
        ('','---------'),
        ('Enano', 'Enano'),
        ('Pequeño', 'Pequeño'),
        ('Mediano', 'Mediano'),
        ('Grande', 'Grande'),
        ('Gigante', 'Gigante'),
    )
    ESTERILIZADO = (
        ('','---------'),
        ('Si', 'Si'),
        ('No', 'No'),
    )
    ESTADOS = (
        ('','---------'),
        ('Normal', 'Normal'),
        ('Perdido', 'Perdido'),
        ('Adopción', 'Adopcion'),
        ('Maltratado', 'Matratado'),
        ('Accidentado', 'Accidentado'),
        ('Encontrado', 'Encontrado'),
    )
    usuario = models.ForeignKey(Profile,on_delete=models.CASCADE,null=False)
    nombre = models.CharField(max_length = 30, blank = False, null = False)
    tipo = models.CharField(max_length = 6, blank = False, null = False, choices = TIPOS)
    fecha_nacimiento = models.DateField('Fecha nacimiento', blank = False, null = False, validators=[validate_current_century])
    sexo = models.CharField(max_length = 7, blank = False, null = False, choices = SEXO)
    raza = models.CharField(max_length = 30, blank = False, null = False, choices = RAZAS)
    color = models.CharField(max_length = 20, blank = False, null = False)
    peso = models.PositiveIntegerField(blank=False, null=False, validators=[MinValueValidator(1),MaxValueValidator(100)])
    tamanio = models.CharField(max_length = 9, blank = False, null = False, choices = TAMANIO)
    enfermedades = models.ManyToManyField(Enfermedad, blank=True)
    enfermedades_gato = models.ManyToManyField(Enfermedad2, blank=True)
    esterilizado = models.CharField(max_length = 3, blank = False, null = False, choices = ESTERILIZADO)
    estado = models.CharField(max_length = 15, blank = False, null = False, choices = ESTADOS)
    foto = models.ImageField(upload_to='mascotas/',default = 'mascotas/anonima.jpg', null = True, blank = True)

    def __str__(self): #To string
        return self.nombre
