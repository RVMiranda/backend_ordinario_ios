from django.contrib import admin
from .models import Calificacion

@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ("estudiante_id", "materia_id", "calificacion", "institucion")
    search_fields = ("estudiante_id", "materia_id", "institucion")
    list_filter = ("institucion",)
