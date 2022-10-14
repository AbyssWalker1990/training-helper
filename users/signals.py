from .models import Profile
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.conf import settings


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email
        )
    # Later ADD send mail


@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()
