from django import forms
from apps.gestor_de_mascotas.forms import DateInput
from .models import Evento_global, Lugar, Conversacion_global, Mensaje
class lugar_form(forms.ModelForm):
 	class Meta:
 		model=Lugar
 		fields=[
 		'nombre_lugar',
        'tipo_lugar',
        'telefono_cel',
        'email',
        'direccion',
 		 ]

 		labels={
 		'nombre_lugar':'Nombre del lugar',
        'tipo_lugar':'Tipo del lugar',
        'telefono_cel':'Telefono de celular del lugar',
        'email':'Correo electrónico del lugar',
        'direccion':'Dirección del lugar',
 		}
 		widgets = {
            #'fecha_evento': DateInput(),
            #'hora_evento': forms.CheckboxSelectMultiple(),
        }
#end class

class evento_global_form(forms.ModelForm):
 	class Meta:
 		model=Evento_global
 		fields=[
 		'nombre_evento',
        'tipo_evento',
        'fecha_evento',
        'hora_evento',
 		 ]

 		labels={
 		'nombre_evento':'Nombre del evento',
        'tipo_evento':'Tipo del evento',
        'fecha_evento':'Fecha del evento',
        'hora_evento':'Hora del evento',
 		}
 		widgets = {
            'fecha_evento': DateInput(),
            'hora_evento': forms.TextInput(attrs={'class': 'form-control', 'type': 'time'}),
        }
#end class

class Conversacion_global_form(forms.ModelForm):
 	class Meta:
 		model=Conversacion_global
 		fields=[
        'titulo',
        'topico',
 		 ]

 		labels={
 		'titulo':'Título de la conversación',
        'topico':'Tópico de la conversación',
 		}
#end class

class Mensaje_form(forms.ModelForm):
 	class Meta:
 		model = Mensaje
 		fields=[
        'contenido',
 		 ]
 		labels={
 		'contenido':'Mensaje',
 		}
#end class
