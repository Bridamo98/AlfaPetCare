from django.shortcuts import render, redirect
from .forms import evento_global_form, lugar_form, Conversacion_global_form, Mensaje_form
from apps.gestor_de_usuarios.models import Profile
from .models import Conversacion_global

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

def crear_conversacion_global(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == "POST":
        conversacion_form = Conversacion_global_form(request.POST)
        if conversacion_form.is_valid():
            conversacion = conversacion_form.save(commit=False)
            conversacion.usuario = profile
            conversacion.save()
            return redirect('index')
    else:
        conversacion_form = Conversacion_global_form()
    return render(request,'crear_conversacion_global.html',{'conversacion_form':conversacion_form,'profile':profile})
#end def

def conversaciones_globales(request):
    profile = Profile.objects.get(user = request.user)
    conversaciones = Conversacion_global.objects.filter(usuario = profile)
    for topico in profile.topicos.all():
        conversaciones_t = Conversacion_global.objects.all().filter(topico = topico)
        conversaciones = conversaciones | conversaciones_t
    return render(request,'conversaciones_globales.html',{'profile':profile,'conversaciones':conversaciones})#HTTP request
#end def

def ver_conversacion(request, conversacion_id):
    profile = Profile.objects.get(user = request.user)
    conversacion = Conversacion_global.objects.get(id = conversacion_id)
    if request.method == "POST":
        mensaje_form = Mensaje_form(request.POST)
        if mensaje_form.is_valid():
            mensaje = mensaje_form.save(commit=False)
            mensaje.usuario = profile
            mensaje.conversacion = conversacion
            mensaje.save()
            return redirect('publicaciones:conversaciones_globales')
    else:
        mensaje_form = Mensaje_form()
    return render(request,'ver_conversacion.html',{'mensaje_form':mensaje_form,'conversacion':conversacion,'profile':profile})

#end def
