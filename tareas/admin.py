from django.contrib import admin
from .models import Tarea

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ("id_tarea", "titulo", "materia", "fecha_entrega", "institucion")
    search_fields = ("id_tarea", "titulo", "materia", "institucion")
    list_filter = ("institucion", "materia")
