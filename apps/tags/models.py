from django.db import models

from apps.posts.models import Post


class Tag(models.Model):
    posts = models.ManyToManyField(
        Post,
        blank=True,
        related_name="tags",
    )
    text = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return self.text
