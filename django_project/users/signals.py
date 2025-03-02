from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# Create Profile when User is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        # This creates a new profile only when a User is created
        Profile.objects.create(user=instance)

# Save Profile when User is saved
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    # This saves the profile after the User is saved
    if hasattr(instance, 'profile'):
        instance.profile.save()
