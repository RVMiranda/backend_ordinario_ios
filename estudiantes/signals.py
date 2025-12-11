from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Estudiante
from .firebase_sync import sync_estudiante_to_firebase

@receiver(post_save, sender=Estudiante)
def sync_estudiante(sender, instance, created, **kwargs):
    sync_estudiante_to_firebase(instance)
