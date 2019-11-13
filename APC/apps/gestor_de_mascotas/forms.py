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
        'raza',
        'color',
        'peso',
        'tamanio',
        'enfermedades',
        'enfermedades_gato',
 		 ]

 		labels={
 		'nombre':'Digite el nombre de la mascota',
        'tipo':'Escoja el tipo de mascota',
        'fecha_nacimiento':'Digite la fecha de nacimiento',
        'sexo':'Escoja el sexo de la mascota',
        'raza':'Escoja la raza de la mascota',
        'color':'Digite el color de la mascota',
        'peso': 'Digite el peso de la mascota (Kg)',
        'tamanio':'Escoja el tamanio de la mascota',
        'enfermedades':'Escoja las enfermedades de la mascota (opcional)',
        'enfermedades_gato':'Escoja las enfermedades de la mascota (opcional)',
 		}
 		widgets = {
            'fecha_nacimiento': DateInput(),
            'enfermedades': forms.CheckboxSelectMultiple(),
            'enfermedades_gato': forms.CheckboxSelectMultiple(),
        }
    #end class
