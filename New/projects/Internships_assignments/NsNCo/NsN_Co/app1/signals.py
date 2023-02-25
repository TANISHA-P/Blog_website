from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Client
from django.dispatch import receiver

@receiver(post_save, sender = User)
def create_client(sender, instance, created, **kwargs):
    if created:
        username = instance.username
        Client.objects.create(Name = username, user = instance)
