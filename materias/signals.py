from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Materia
from .firebase_sync import sync_materia_to_firebase, delete_materia_from_firebase

@receiver(post_save, sender=Materia)
def sync_materia(sender, instance, created, **kwargs):
    sync_materia_to_firebase(instance)

@receiver(post_delete, sender=Materia)
def delete_materia(sender, instance, **kwargs):
    delete_materia_from_firebase(instance)
