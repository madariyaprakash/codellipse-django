# once user save the data this post_save will fired
from django.db.models.signals import post_save
# this Use model will be sender
from django.contrib.auth.models import User
# We also need receiver
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
# we need to create profile object for every user registeration

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

# we need to import sginals under ready function to app.py