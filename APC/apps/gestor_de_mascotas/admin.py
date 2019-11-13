from django.contrib import admin

from .models import Mascota, Enfermedad, Enfermedad2#Para visualizarlo en ADMIN


admin.site.register(Mascota)
admin.site.register(Enfermedad)
admin.site.register(Enfermedad2)
