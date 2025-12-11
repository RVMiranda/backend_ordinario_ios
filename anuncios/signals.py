from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Anuncio
from .firebase_sync import sync_anuncio_to_firebase, delete_anuncio_from_firebase

@receiver(post_save, sender=Anuncio)
def sync_anuncio(sender, instance, created, **kwargs):
    sync_anuncio_to_firebase(instance)

@receiver(post_delete, sender=Anuncio)
def delete_anuncio(sender, instance, **kwargs):
    delete_anuncio_from_firebase(instance)
