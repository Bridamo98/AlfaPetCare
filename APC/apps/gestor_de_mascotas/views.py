from django.shortcuts import render
from .forms import registro_mascota_form
from apps.gestor_de_usuarios.models import Profile
from django.shortcuts import render, redirect

# Create your views here.
"""
Entradas: request, petición del usuario
proceso: valida y efectua el registro de una mascota
Salidas: pantalla de inicio, en caso de ser correcta la agregación
"""
def registro_mascota(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == "POST":
        mascota_form = registro_mascota_form(request.POST, request.FILES)
        if mascota_form.is_valid():
            mascota=mascota_form.save(commit=False)
            mascota.usuario = profile
            mascota.save()
            mascota_form.save_m2m()
            return redirect('index')
    else:
        mascota_form = registro_mascota_form()
    return render(request,'registro_mascota.html',{'mascota_form':mascota_form,'profile':profile})
#end def
"""
Entradas: request, petición del usuario
proceso: renderiza el listado de las mascotas
Salidas: pantalla de lista de mascotas
"""
def mis_mascotas(request):
    profile = Profile.objects.get(user = request.user)
    mascotas = profile.mascota_set.all()
    return render(request,'mis_mascotas.html',{'profile':profile,'mascotas':mascotas})
#end def
