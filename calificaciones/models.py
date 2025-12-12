from django.db import models
from estudiantes.models import Estudiante
from materias.models import Materia
from whitelabel.models import Institution  # Asegúrate de importar la institución desde el modelo adecuado.

class Calificacion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, null=True, blank=True)  # Relaciona con Estudiante
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, null=True, blank=True)        # Relaciona con Materia
    calificacion = models.PositiveIntegerField()                           # La calificación numérica (entero)
    institucion = models.ForeignKey(Institution, on_delete=models.CASCADE)  # Relaciona con Institución

    class Meta:
        unique_together = ("estudiante", "materia")  # Asegura que no haya duplicados

    def __str__(self):
        return f"{self.estudiante} → {self.materia}: {self.calificacion}"