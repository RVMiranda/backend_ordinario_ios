from django.db import models
from whitelabel.models import Institution

class Anuncio(models.Model):
    id_anuncio = models.CharField(max_length=20, unique=True)  # anuncio_001
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha = models.DateField()

    institucion = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name="anuncios")

    def __str__(self):
        return f"{self.titulo} ({self.institucion})"
