from django import forms
from apps.gestor_de_mascotas.forms import DateInput
from .models import Evento_global, Conversacion_global, Mensaje, Evento_personal

class evento_global_form(forms.ModelForm):
  class Meta:
    model = Evento_global
    # datetime-local is a HTML5 input type, format to make date time show on fields
    fields = [
        'nombre_evento',
        'tipo_evento',
        'fecha_hora_evento_inicio',
        'fecha_hora_evento_final',
        'direccion',
        'longitud',
        'latitud',
    ]
    labels = {
        'nombre_evento':'Nombre del evento',
        'tipo_evento':'Tipo del evento',
        'fecha_hora_evento_inicio':'Fecha y hora del inicio del evento',
        'fecha_hora_evento_final':'Fecha y hora del final del evento',
        'Direccion':'Direccion del evento',
        'longitud':'',
        'latitud':'',
    }
    widgets = {
      'fecha_hora_evento_inicio': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'fecha_hora_evento_final': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }

  def __init__(self, *args, **kwargs):
    super(evento_global_form, self).__init__(*args, **kwargs)
    # input_formats to parse HTML5 datetime-local input to datetime field
    self.fields['fecha_hora_evento_inicio'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['fecha_hora_evento_final'].input_formats = ('%Y-%m-%dT%H:%M',)
#end class

class evento_personal_form(forms.ModelForm):
  class Meta:
    model = Evento_personal
    # datetime-local is a HTML5 input type, format to make date time show on fields
    fields = [
        'tipo_evento',
        'fecha_hora_evento',
    ]
    labels = {
        'tipo_evento':'Tipo del evento',
        'fecha_hora_evento':'Fecha y hora del evento',
    }
    widgets = {
      'fecha_hora_evento': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }

  def __init__(self, *args, **kwargs):
    super(evento_personal_form, self).__init__(*args, **kwargs)
    # input_formats to parse HTML5 datetime-local input to datetime field
    self.fields['fecha_hora_evento'].input_formats = ('%Y-%m-%dT%H:%M',)
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
