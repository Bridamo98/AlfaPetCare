from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from .models import Profile, Servicio

class FormularioLogin(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super(FormularioLogin,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

class RegistroForm(UserCreationForm):
	class Meta:
		model= User
		fields=[
		'username',
		'first_name',
		'last_name',
		'email',
        ]
		labels={
		'username':'Nombre de Usuario',
		'first_name':'Nombres',
		'last_name': 'Apellidos',
		'email':'Correo electronico',
		}

class infoForm(forms.ModelForm):
 	class Meta:
 		model=Profile
 		fields=[
 		'tfno',
        'foto',
 		 ]

 		labels={
 		'tfno':'Digitar numero telefonico (opcional)',
 		   }
 		widgets={

 		}

class editar_perfil_form(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        ]
        labels={
		'username':'Nombre de Usuario',
		'first_name':'Nombres',
		'last_name': 'Apellidos',
		'email':'Correo electronico',
		}

class editar_informacion_form(UserChangeForm):
    password = None
    class Meta:
        model = Profile
        fields = [
        'tfno',
        'foto'
        ]
        labels={
 		'tfno':'Número telefónico',
 		}


class agregar_topicos_form(forms.ModelForm):
 	class Meta:
 		model=Profile
 		fields=[
 		'topicos',
 		 ]

 		labels={
        'topicos':'Escoja TODOS los tópicos que quiera tener',
 		}
 		widgets = {
            'topicos': forms.CheckboxSelectMultiple(),
        }
    #end class

class agregar_servicio_form(forms.ModelForm):
 	class Meta:
 		model=Servicio
 		fields=[
 		'tipo',
 		'direccion',
        'longitud',
        'latitud',
 		 ]

 		labels={
 		'tipo':'Seleccione el tipo de servicio',
 		'direccion':'Dirección del proveedor',
        'longitud':'',#------
        'latitud':'',#------
 		}
 		widgets = {

        }
    #end class
#end-class
