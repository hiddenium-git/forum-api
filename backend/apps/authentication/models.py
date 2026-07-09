from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(
        upload_to='avatars/',
        null=True,
        blank=True,
    )

    bio = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    email = models.EmailField(
        blank=False
    )
