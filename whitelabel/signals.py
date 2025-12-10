from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Institution
from .firebase_sync import sync_institution_to_firebase

@receiver(post_save, sender=Institution)
def sync_institution(sender, instance, created, **kwargs):
    sync_institution_to_firebase(instance)
