from django.db import models
from whitelabel.models import Institution

class Materia(models.Model):
    id_materia = models.CharField(max_length=20, unique=True)  # mat_001
    nombre = models.CharField(max_length=100)
    profesor = models.CharField(max_length=100)
    institucion = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name="materias")

    # Lista de tareas asociadas (solo almacenamos IDs de Firebase)
    tareas = models.JSONField(default=dict, blank=True)  # {"tarea_001": true}

    # Calificaciones por estudiante (referencias a Firebase)
    calificaciones = models.JSONField(default=dict, blank=True)  # {"est_001": 95}

    def __str__(self):
        return f"{self.nombre} ({self.id_materia})"