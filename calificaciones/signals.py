from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Calificacion
from .firebase_sync import sync_calificacion_to_firebase, delete_calificacion_from_firebase

@receiver(post_save, sender=Calificacion)
def sync_calificacion(sender, instance, created, **kwargs):
    sync_calificacion_to_firebase(instance)

@receiver(post_delete, sender=Calificacion)
def delete_calificacion(sender, instance, **kwargs):
    delete_calificacion_from_firebase(instance)
