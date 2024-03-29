from django.shortcuts import render
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout, update_session_auth_hash
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from apps.publicaciones.models import Evento_global
from .forms import *

from .models import Profile
"""
Entradas: request, petición del usuario
proceso: Renderiza la página de inicio
Salidas: profile, información asociada al usuario
"""
def Home(request):
    if(request.user.is_staff):
        return HttpResponseRedirect('/admin/')
    
    profile = Profile.objects.get(user = request.user)
    eventos = Evento_global.objects.all()
    return render(request,'index.html',{'profile':profile,'eventos':eventos})#HTTP request
#end def
"""
Entradas: FormView, formulario de login
proceso: Renderiza el formulario de login y valida el login
Salidas: pantalla de inicio, en caso de que el login sea correcto
"""
class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)

    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return self.HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request,*args,**kwargs)
        #end if
    #end def

    def form_valid(self,form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)
#end class
"""
Entradas: request, petición del usuario
proceso: efectua el logout del usuario
Salidas: pantalla de login
"""
def Logout(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login')
#end def
"""
Entradas: request, petición del usuario
proceso: valida y efectua el registro de un usuario
Salidas: pantalla de login, en caso de ser correcto el registro
"""
def Registro(request):
    if request.method == "POST":
        user_form = RegistroForm(request.POST)
        info_form = infoForm(request.POST, request.FILES)
        if user_form.is_valid() and info_form.is_valid():
            user=user_form.save(commit=False)
            profile=info_form.save(commit=False)
            user.save()
            profile.user=user
            profile.save()
            return redirect('login')
    else:
        user_form= RegistroForm()
        info_form=infoForm()
    return render(request,'registro.html',{'user_form':user_form,'info_form':info_form})
#end def
"""
Entradas: request, petición del usuario
proceso: valida y efectua el cambio en la information de un usuario
Salidas: pantalla de inicio, en caso de ser correcto la modificación
"""
def Editar_perfil(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == "POST":
        edit_user_form = editar_perfil_form(request.POST, instance = request.user)
        edit_info_form = editar_informacion_form(request.POST, request.FILES, instance = profile)
        #edit_password_form = PasswordChangeForm(data = request.POST, user = request.user)
        if edit_user_form.is_valid() and edit_info_form.is_valid():
            edit_user_form.save()
            edit_info_form.save()
            #edit_password_form.save()
            return redirect('index')
    else:
        edit_user_form = editar_perfil_form(instance = request.user)
        edit_info_form = editar_informacion_form(instance = profile)
        #edit_password_form = PasswordChangeForm(user = request.user)
    return render(request,'editar_perfil.html',{'edit_user_form':edit_user_form,'edit_info_form':edit_info_form,'profile':profile,})#HTTP request
"""
Entradas: request, petición del usuario
proceso: valida y efectua el cambio de contraseña de un usuario
Salidas: pantalla de editar perfil, en caso de ser correcto el cambio
"""
def Cambiar_password(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == "POST":
        edit_password_form = PasswordChangeForm(data = request.POST, user = request.user)
        if edit_password_form.is_valid():
            edit_password_form.save()
            update_session_auth_hash(request, edit_password_form.user)
            return redirect('editar_perfil')
        else:
            return redirect ('cambiar_password')
    else:
        edit_password_form = PasswordChangeForm(user = request.user)
    return render(request,'cambiar_password.html',{'edit_password_form':edit_password_form,'profile':profile,})#HTTP request
"""
Entradas: request, petición del usuario
proceso: renderiza la pantalla de topicos del usuario
Salidas: pantalla de topicos
"""
def Topicos(request):
    profile = Profile.objects.get(user = request.user)
    return render(request,'topicos.html',{'profile':profile,})#HTTP request
#end def
"""
Entradas: request, petición del usuario
proceso: valida y efectua el agregar topicos de un usuario
Salidas: pantalla de topicos del usuario, en caso de ser correcta la agregación
"""
def Agregar_topicos(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == "POST":
        a_topicos_form = agregar_topicos_form(request.POST, instance = profile)
        if a_topicos_form.is_valid():
            a_topicos_form.save()
            return redirect('topicos')
    else:
        a_topicos_form = agregar_topicos_form()
    return render(request,'agregar_topicos.html',{'agregar_topicos_form':agregar_topicos_form,'profile':profile,})#HTTP request
#end def
"""
Entradas: request, petición del usuario
proceso: valida y efectua el agregar servicios de un usuario
Salidas: pantalla de inicio, en caso de ser correcta la agregación
"""
def Agregar_servicio(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == "POST":
        servicio_form = agregar_servicio_form(request.POST)
        if servicio_form.is_valid():
            servicio = servicio_form.save(commit=False)
            servicio.usuario=profile
            servicio.save()
            return redirect('index')
    else:
        servicio_form = agregar_servicio_form()
    return render(request,'agregar_servicio.html',{'servicio_form':servicio_form,'profile':profile,})#HTTP request
#end def
