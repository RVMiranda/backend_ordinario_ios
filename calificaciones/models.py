from django.db import models

class Calificacion(models.Model):
    estudiante_id = models.CharField(max_length=20)   # est_001
    materia_id = models.CharField(max_length=20)      # mat_001

    # La calificación numérica (entero)
    calificacion = models.PositiveIntegerField()

    # Para instituciones en caso de whitelabel
    institucion = models.CharField(max_length=50)

    class Meta:
        unique_together = ("estudiante_id", "materia_id")  # Evita duplicados

    def __str__(self):
        return f"{self.estudiante_id} → {self.materia_id}: {self.calificacion}"
