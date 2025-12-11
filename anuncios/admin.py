from django.contrib import admin
from .models import Anuncio

@admin.register(Anuncio)
class AnuncioAdmin(admin.ModelAdmin):
    list_display = ("id_anuncio", "titulo", "fecha", "institucion")
    search_fields = ("id_anuncio", "titulo", "institucion")
    list_filter = ("institucion", "fecha")
