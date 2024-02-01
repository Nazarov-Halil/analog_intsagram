from django.db import models
from apps.users.models import User
from apps.posts.models import Post


class Comment(models.Model):
    text = models.TextField(

    )
    date = models.DateTimeField(
        auto_now_add=True
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name='comment'
    )

    def __str__(self):           
        return self.user.username


