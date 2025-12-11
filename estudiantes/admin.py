from django.contrib import admin
from .models import Estudiante

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ("usuario", "matricula", "institucion", "firebase_key")
    search_fields = ("usuario__username", "matricula", "firebase_key")
    list_filter = ("institucion",)