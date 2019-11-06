from django.contrib import admin

from .models import Mascota, Enfermedad#Para visualizarlo en ADMIN


admin.site.register(Mascota)
admin.site.register(Enfermedad)
