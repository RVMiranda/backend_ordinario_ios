from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from .firebase_sync import sync_user_to_firebase

@receiver(post_save, sender=User)
def create_or_update_user_firebase(sender, instance, created, **kwargs):
    sync_user_to_firebase(instance)
