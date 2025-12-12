from django.db import models
from whitelabel.models import Institution
from materias.models import Materia

class Tarea(models.Model):
    id_tarea = models.CharField(max_length=20, unique=True)  # tarea_001
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_entrega = models.DateField()

    #materia = models.CharField(max_length=20)       # mat_001 (id en Firebase)
    #institucion = models.CharField(max_length=50)   # institucion_1

    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name="tareas_asociadas")
    institucion = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name="tareas")

    ESTADO_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('completada', 'Completada'),
    )
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')

    def __str__(self):
        return f"{self.titulo} ({self.estado})"
