from django.contrib import admin
from .models import Institution

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ("nombre", "firebase_key", "mostrar_anuncios", "mostrar_tareas", "mostrar_calificaciones")
    search_fields = ("nombre", "firebase_key")

    fieldsets = (
        ("Identidad", {
            "fields": ("firebase_key", "nombre", "logo_url")
        }),
        ("Colores", {
            "fields": ("color_primario", "color_secundario", "color_fondo", "color_texto")
        }),
        ("Textos", {
            "fields": ("texto_bienvenida", "texto_descripcion")
        }),
        ("Configuración de módulos", {
            "fields": ("mostrar_anuncios", "mostrar_tareas", "mostrar_calificaciones")
        }),
    )
