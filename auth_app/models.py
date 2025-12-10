from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Administrador'),
        ('teacher', 'Profesor'),
        ('student', 'Estudiante'),
    )
    # Identificador de la institución (del whitelabel)
    institucion = models.CharField(max_length=100, default="institucion_1")
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')

    # Campo para sincronización con Firebase
    firebase_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.institucion})"
