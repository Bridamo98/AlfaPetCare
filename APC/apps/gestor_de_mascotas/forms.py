from django import forms
from .models import Mascota, Enfermedad


class DateInput(forms.DateInput):
    input_type = 'date'

class registro_mascota_form(forms.ModelForm):
 	class Meta:
 		model=Mascota
 		fields=[
 		'nombre',
        'tipo',
        'fecha_nacimiento',
        'sexo',
        #'enfermedades',
 		 ]

 		labels={
 		'nombre':'Digite el nombre de la mascota',
        'tipo':'Escoja el tipo de mascota',
        'fecha_nacimiento':'Digite la fecha de nacimiento',
        'sexo':'Escoja el sexo de la mascota',
        #'enfermedades':'Escoja las enfermedades de la mascota',
 		}
 		widgets = {
            'fecha_nacimiento': DateInput(),
        }
    #end class
