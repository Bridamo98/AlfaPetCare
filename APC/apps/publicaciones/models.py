from datetime import datetime, timedelta
from calendar import HTMLCalendar
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
    nombre_lugar = models.CharField(max_length = 256, blank = False, null = False)
    tipo_lugar = models.CharField(max_length = 256, blank = False, null = False, choices = TIPOS)
    telefono_cel = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(1000000),MaxValueValidator(9999999999)])
    email = models.EmailField(max_length = 256, blank = False, null = False)
    direccion = models.CharField(max_length = 256, blank = False, null = False)
    longitud = models.FloatField(null=True, blank=True, default=None)#------
    latitud = models.FloatField(null=True, blank=True, default=None)#------
    def __str__(self): #To string
        return self.nombre_lugar



class Evento_global(models.Model):
    TIPOS = (
        ('Global', 'Global'),
        ('Personal', 'Personal'),
    )
    usuario = models.ForeignKey(Profile,on_delete=models.CASCADE,null=False)
    nombre_evento = models.CharField(max_length = 256, blank = False, null = False)
    tipo_evento = models.CharField(max_length = 256, blank = False, null = False, choices = TIPOS)
    fecha_hora_evento_inicio = models.DateTimeField(auto_now=False, auto_now_add=False, default = None)
    fecha_hora_evento_final = models.DateTimeField(auto_now=False, auto_now_add=False, default = None)
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

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None, locale='fr_FR'):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()
	# formats a day as a td
	# filter events by day
	def formatday(self, day, events):
		events_per_day = events.filter(fecha_hora_evento_inicio__day=day)
		d = ''
		for event in events_per_day:
			d += f'<li> {event.nombre_evento} </li>'

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul style = 'height: 100%;padding: 0px 5px 0px 20px;'> {d} </ul></td>"
		return '<td></td>'

	# formats a week as a tr
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		events = Evento_global.objects.filter(fecha_hora_evento_inicio__year=self.year, fecha_hora_evento_inicio__month=self.month)
		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		return cal
