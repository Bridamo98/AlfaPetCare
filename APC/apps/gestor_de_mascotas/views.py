from django.shortcuts import render
from .forms import registro_mascota_form
from apps.gestor_de_usuarios.models import Profile
from django.shortcuts import render, redirect

# Create your views here.
"""
Valida y renderiza el registro de una mascota
"""
def registro_mascota(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == "POST":
        mascota_form = registro_mascota_form(request.POST)
        if mascota_form.is_valid():
            profile = Profile.objects.get(user = request.user)
            mascota=mascota_form.save(commit=False)
            mascota.usuario = profile
            mascota.save()
            return redirect('index')
    else:
        mascota_form = registro_mascota_form()
    return render(request,'registro_mascota.html',{'mascota_form':mascota_form,'profile':profile})
#end def
