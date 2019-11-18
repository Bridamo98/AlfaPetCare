from datetime import datetime, timedelta, date
import calendar

from django.shortcuts import render, redirect
from .forms import evento_global_form, Conversacion_global_form, Mensaje_form, evento_personal_form

from django.views import generic
from django.http import HttpResponse
from django.utils.safestring import mark_safe

from apps.gestor_de_usuarios.models import Profile
from .models import *
from .filters import Conversacion_filter
"""
Entradas: request, petición del usuario
proceso: valida y efectua el agregar un evento global de un usuario
Salidas: pantalla de inicio, en caso de ser correcta la agregación
"""
def agregar_evento_global(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == "POST":
        evento_form = evento_global_form(request.POST)
        if evento_form.is_valid():
            evento = evento_form.save(commit=False)
            evento.usuario = profile
            evento.save()
            return redirect('index')
    else:
        evento_form = evento_global_form()
    return render(request,'agregar_evento_global.html',{'evento_form':evento_form})
#end def
"""
Entradas: request, petición del usuario
proceso: valida y efectua el agregar un evento personal de un usuario
Salidas: pantalla de inicio, en caso de ser correcta la agregación
"""
def agregar_evento_personal(request, mascota_id):
    profile = Profile.objects.get(user = request.user)
    mascota = Mascota.objects.get(id = mascota_id)
    if request.method == "POST":
        evento_form = evento_personal_form(request.POST)
        if evento_form.is_valid():
            evento = evento_form.save(commit=False)
            evento.mascota = mascota
            evento.usuario = profile
            evento.save()
            return redirect('index')
    else:
        evento_form = evento_personal_form()
    return render(request,'agregar_evento_personal.html',{'evento_form':evento_form})
#end def
"""
Entradas: request, petición del usuario
proceso: valida y efectua el agregar una conversacion global de un usuario
Salidas: pantalla de inicio, en caso de ser correcta la agregación
"""
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
"""
Entradas: request, petición del usuario
proceso: lista las conversaciones globales pertenecientes a un usuario
Salidas: pantalla que contiene las conversaciones globales
"""
def conversaciones_globales(request):
    profile = Profile.objects.get(user = request.user)
    conversaciones = Conversacion_global.objects.filter(usuario = profile)
    for topico in profile.topicos.all():
        conversaciones_t = Conversacion_global.objects.all().filter(topico = topico)
        conversaciones = conversaciones | conversaciones_t
    return render(request,'conversaciones_globales.html',{'profile':profile,'conversaciones':conversaciones})#HTTP request
#end def
"""
Entradas: request, petición del usuario e id de la conversación elegida
proceso: muestra la información relacionada a una conversación global
Salidas: pantalla de información de la conversación seleccionada
"""
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
            return render(request,'ver_conversacion.html',{'mensaje_form':mensaje_form,'conversacion':conversacion,'profile':profile})
    else:
        mensaje_form = Mensaje_form()
    return render(request,'ver_conversacion.html',{'mensaje_form':mensaje_form,'conversacion':conversacion,'profile':profile})

#end def
"""
Representa el calendario que contiene los eventos conversaciones_globales
atributos:
-model = La clase que se mostrará en el calendario_global
-template_name = nombre del template donde se renderizará el calendario
"""
class CalendarView(generic.ListView):
    model = Evento_global
    template_name = 'calendario_global.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def buscar_conversacion_global(request):
    profile = Profile.objects.get(user = request.user)
    conversaciones = Conversacion_global.objects.filter(usuario = profile)
    for topico in profile.topicos.all():
        conversaciones_t = Conversacion_global.objects.all().filter(topico = topico)
        conversaciones = conversaciones | conversaciones_t
    return render(request,'conversaciones_globales.html',{'profile':profile,'conversaciones':conversaciones})#HTTP request
#end def
"""
Representa la clase que se encarga de gestionar el filtrado de conversaciones(buscador de conversaciones)
atributos:
-model = La clase que se filtrará
-template_name = nombre del template donde se renderizará el listado de conversaciones resultantes
"""
class Conversaciones_ListView(generic.ListView):
    model = Conversacion_global
    template_name = 'conversaciones_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = Conversacion_filter(self.request.GET, queryset = self.get_queryset())
        return context
"""
Representa el calendario que contiene los eventos conversaciones personales
atributos:
-model = La clase que se mostrará en el calendario personal
-template_name = nombre del template donde se renderizará el calendario
"""
class Calendario_personal(generic.ListView):
    model = Evento_personal
    template_name = 'calendario_personal.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        profile = Profile.objects.get(user = self.request.user)
        cal = Calendar2(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True, prof=profile)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context
