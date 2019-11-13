from django.shortcuts import render, redirect
from .forms import evento_global_form, lugar_form
from apps.gestor_de_usuarios.models import Profile

def agregar_evento_global(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == "POST":
        evento_form = evento_global_form(request.POST)
        sitio_form = lugar_form(request.POST)
        if evento_form.is_valid() and sitio_form.is_valid():

            lugar = sitio_form.save(commit=False)
            lugar.save()
            evento = evento_form.save(commit=False)
            evento.usuario = profile
            evento.lugar = lugar

            evento.save
            return redirect('index')
    else:
        evento_form = evento_global_form()
        sitio_form = lugar_form()
    return render(request,'agregar_evento_global.html',{'evento_form':evento_form,'sitio_form':sitio_form})
#end def

# Create your views here.
