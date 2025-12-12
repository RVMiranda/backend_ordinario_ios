from django.db import models
from auth_app.models import User
from whitelabel.models import Institution

class Estudiante(models.Model):
    firebase_key = models.CharField(
        max_length=100,
        unique=True,
        help_text="Clave con la que se sincroniza en Firebase (ejemplo: est_001)"
    )

    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="perfil_estudiante"
    )

    matricula = models.CharField(max_length=50, unique=True)
    institucion = models.ForeignKey(
        Institution,
        on_delete=models.CASCADE,
        related_name="estudiantes"
    )

    # Nuevo campo: Nombre del estudiante
    nombre = models.CharField(max_length=100)

    # Nuevo campo: Correo del estudiante
    correo = models.EmailField(max_length=255)

    # Nuevo campo: Carrera del estudiante
    carrera = models.CharField(max_length=100)

    # Nuevo campo: Foto opcional del estudiante
    foto = models.ImageField(upload_to='estudiantes/', null=True, blank=True)


    def __str__(self):
        return f"{self.usuario.username} - {self.matricula}"