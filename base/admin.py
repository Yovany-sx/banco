from django.contrib import admin
from .models import Country, City, Municipality, State, Parish
from person.models import Factor, Grupo_sanguineo
from noticia.models import Noticia

admin.site.register(Country)
admin.site.register(State)
admin.site.register(Parish)
admin.site.register(Municipality)
admin.site.register(Factor)
admin.site.register(Grupo_sanguineo)
admin.site.register(Noticia)