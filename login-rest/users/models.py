import uuid
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


@python_2_unicode_compatible
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Name", max_length=255, blank=True, null=True)
    picture = models.ImageField('Profile picture',
                                upload_to='profile_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    bio = models.CharField("Short Bio", max_length=200, blank=True, null=True)
    phone = models.CharField("Phone", max_length=20, blank=True, null=True)
    address = models.CharField("Address", max_length=200, blank=True, null=True)
    zip_code = models.CharField(
        "ZIP / Postal code",
        max_length=12,
        blank=True, 
        null=True
    )

    city = models.CharField(
        "City",
        max_length=200,
        blank=True, 
        null=True
    )

    country = models.CharField(
        "Country",
        max_length=30,
        blank=True, 
        null=True
    )

    photo_id = models.ImageField('Profile picture',
                                upload_to='photo_ids/%Y-%m-%d/',
                                null=True,
                                blank=True)

    consumer = 'CMR'
    marchent = 'MCT'
    organization = 'ORG'

    PROFILE_TYPE = (
        (consumer, "Consumer"),
        (marchent, "Marchent"),
        (organization, "Organization"),
    )

    profile_type = models.CharField(
        "Profile Type",
        max_length=3,
        choices=PROFILE_TYPE,
        default=consumer,
    )


    def __str__(self):
        return self.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
