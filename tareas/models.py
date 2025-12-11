from django.db import models

class Tarea(models.Model):
    id_tarea = models.CharField(max_length=20, unique=True)  # tarea_001
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_entrega = models.DateField()

    materia = models.CharField(max_length=20)       # mat_001 (id en Firebase)
    institucion = models.CharField(max_length=50)   # institucion_1

    def __str__(self):
        return f"{self.titulo} ({self.id_tarea})"
