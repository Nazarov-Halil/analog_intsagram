from django.db import models
from apps.users.models import User
from apps.posts.models import Post
from apps.comments.models import Comment


class LikePost(models.Model):
    object = None
    count = models.IntegerField(
        default=0
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_like')

    def __str__(self):
        return self.post.location


class LikeComment(models.Model):
    count = models.IntegerField(
        default=0
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_like')

    def __str__(self):
        return self.comment.text
