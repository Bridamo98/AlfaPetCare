from django.shortcuts import render
from apps.gestor_de_usuarios.models import Profile
def Mapa(request):
    profile = Profile.objects.get(user = request.user)
    return render(request,'mapa.html',{'profile':profile,})#HTTP request
#end def
