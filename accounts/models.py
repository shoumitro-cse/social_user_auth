from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.contants import MALE, FEMALE, OTHERS, OWNER, \
						ADMIN, MODERATOR, CLIENT, ISLAM, HINDU, \
						BUDDHA, CHRISTIAN


GENDER_CHOICES = (
    (MALE, "MALE"),
    (FEMALE, "FEMALE"),
    (OTHERS, "OTHERS"),
)


USER_TYPE_CHOICES = (
    (OWNER, "OWNER"),
    (ADMIN, "ADMIN"),
    (MODERATOR, "MODERATOR"),
    (CLIENT, "CLIENT"),
)


RELIGION_TYPE_CHOICES = (
    (ISLAM, "ISLAM"),
    (HINDU, "HINDU"),
    (BUDDHA, "BUDDHA"),
    (CHRISTIAN, "CHRISTIAN"),
)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(BaseModel, AbstractUser):
    username = models.CharField(unique=True, max_length=255)
    email = models.EmailField(blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True)
    is_staff = models.BooleanField(default=False)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True, blank=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=CLIENT)
    
    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    address = models.TextField(blank=True)
    religion = models.PositiveSmallIntegerField(choices=RELIGION_TYPE_CHOICES, blank=True, null=True)
    profile_image = models.ImageField(upload_to="profile/", default='profile/default.jpeg')
    cover_image = models.ImageField(upload_to="cover_image/", default='profile/default.jpeg')

    class Meta:
        verbose_name = "profile"
        verbose_name_plural = "profiles"



