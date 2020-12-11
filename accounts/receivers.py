from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, *args, **kwargs):
    if created:
        profile = Profile(
            user=instance,
            userPhotoURL="image/upload/v1607681887/events/user-photos/user-default.jpg"
        )
        profile.save()
