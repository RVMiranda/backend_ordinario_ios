from django.contrib import admin
from .models import Materia

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ("id_materia", "nombre", "profesor", "institucion")
    search_fields = ("id_materia", "nombre", "profesor")
