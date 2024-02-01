from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.TextField(
        max_length=250,
        verbose_name="Биография",
        blank=True,
        null=True,
    )
    avatar = models.ImageField(
        upload_to="users-avatar/",
        verbose_name="Аватарка",
        blank=True,
        null=True,
    )
    external_link = models.URLField(
        verbose_name="Ссылка",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.username
