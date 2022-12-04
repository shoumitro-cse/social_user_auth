from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from accounts.models import Profile

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_information(sender, instance=None, created=False, **kwargs):
    if created:
        Profile.objects.create(user=instance)

