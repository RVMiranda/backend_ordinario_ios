from django.db import models

class Anuncio(models.Model):
    id_anuncio = models.CharField(max_length=20, unique=True)  # anuncio_001
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha = models.DateField()

    institucion = models.CharField(max_length=50)  # institucion_1

    def __str__(self):
        return f"{self.titulo} ({self.institucion})"
