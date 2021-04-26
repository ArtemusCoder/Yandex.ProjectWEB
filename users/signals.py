from django.db.models.signals import post_save, pre_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
import os
import uuid


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(pre_save, sender=Profile)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = Profile.objects.get(pk=instance.pk).image
    except Profile.DoesNotExist:
        return False

    if old_file.name == "default.jpg":
        return False

    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

@receiver(pre_delete, sender=Profile)
def del_info_User(sender, instance, **kwargs):
    image = Profile.objects.get(pk=instance.pk).image
    if not image.name == "default.jpg":
        os.remove(image.path)