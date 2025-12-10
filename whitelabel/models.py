from django.db import models

class Institution(models.Model):
    firebase_key = models.CharField(
        max_length=100,
        unique=True,
        help_text="Clave con la que se sincroniza en Firebase (ejemplo: institucion_1)"
    )

    nombre = models.CharField(max_length=200)
    logo_url = models.URLField(blank=True, null=True)

    # Colores
    color_primario = models.CharField(max_length=10, default="#1A73E8")
    color_secundario = models.CharField(max_length=10, default="#185ABC")
    color_fondo = models.CharField(max_length=10, default="#F5F5F5")
    color_texto = models.CharField(max_length=10, default="#000000")

    # Textos
    texto_bienvenida = models.CharField(max_length=300, blank=True, null=True)
    texto_descripcion = models.CharField(max_length=500, blank=True, null=True)

    # Configuraciones
    mostrar_anuncios = models.BooleanField(default=True)
    mostrar_calificaciones = models.BooleanField(default=True)
    mostrar_tareas = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} ({self.firebase_key})"