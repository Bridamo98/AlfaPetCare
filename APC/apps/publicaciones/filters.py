import django_filters
from apps.publicaciones.models import Conversacion_global

class Conversacion_filter(django_filters.FilterSet):
    class Meta:
        model = Conversacion_global
        fields = {
            'titulo': ['icontains'],
        }
