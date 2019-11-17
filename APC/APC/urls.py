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
from django.conf.urls import url
from apps.gestor_de_usuarios.views import Home#para la clase requerida
from django.contrib.auth.decorators import login_required
from apps.gestor_de_usuarios.views import Login, Logout, Registro, Topicos, Agregar_topicos, Editar_perfil, Cambiar_password, Agregar_servicio
from apps.mapa.views import Mapa

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings # new

from apps.publicaciones.views import CalendarView, Calendario_personal


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('prueba/', include(('apps.prueba.urls','prueba'))),#Enlazar una url de app con la del proyecto
    path('',login_required(Home) ,name = 'index'),#(1)Texto para ejecutar codigo de clase (2), y (3) solo para template django
    path('accounts/login/',Login.as_view(),name = 'login'),
    path('logout/',login_required(Logout), name = 'logout'),
    path('registro/',Registro, name = 'registro'),
    path('mapa/',login_required(Mapa), name = 'mapa'),
    path('mascota/',include(('apps.gestor_de_mascotas.urls','mascota'))),
    path('topicos/',login_required(Topicos), name = 'topicos'),
    path('topicos/agregar_topicos/',login_required(Agregar_topicos), name = 'agregar_topicos'),
    path('editar_perfil/',login_required(Editar_perfil), name = 'editar_perfil'),
    path('editar_perfil/cambiar_contraseña/',login_required(Cambiar_password), name = 'cambiar_password'),
    path('agregar_servicio/',login_required(Agregar_servicio), name = 'agregar_servicio'),
    path('publicaciones/', include(('apps.publicaciones.urls','publicaciones'))),#Enlazar una url de app con la del proyecto
    url(r'^calendar/$', CalendarView.as_view(), name='calendar'),
    url(r'^calendario_personal/$', Calendario_personal.as_view(), name='calendario_personal'),


]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
