"""APC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.gestor_de_usuarios.views import Home#para la clase requerida
from django.contrib.auth.decorators import login_required
from apps.gestor_de_usuarios.views import Login, Logout, Registro
from apps.mapa.views import Mapa

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('prueba/', include(('apps.prueba.urls','prueba'))),#Enlazar una url de app con la del proyecto
    path('',login_required(Home) ,name = 'index'),#(1)Texto para ejecutar codigo de clase (2), y (3) solo para template django
    path('accounts/login/',Login.as_view(),name = 'login'),
    path('logout/',login_required(Logout), name = 'logout'),
    path('registro/',Registro, name = 'registro'),
    path('mapa/',login_required(Mapa), name = 'mapa'),
]
