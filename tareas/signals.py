from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Tarea
from .firebase_sync import sync_tarea_to_firebase, delete_tarea_from_firebase

@receiver(post_save, sender=Tarea)
def sync_tarea(sender, instance, created, **kwargs):
    sync_tarea_to_firebase(instance)

@receiver(post_delete, sender=Tarea)
def delete_tarea(sender, instance, **kwargs):
    delete_tarea_from_firebase(instance)
