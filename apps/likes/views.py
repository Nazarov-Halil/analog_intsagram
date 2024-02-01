from django.shortcuts import redirect, render
from django.views import View
from apps.likes.models import LikePost
from apps.comments.forms import Comment
from apps.users.models import User


class AddLikeView(View):
    template_name = 'test.html'

    def post(self, *args, **kwargs):
        blog_post_id = int(self.POST.get('blog_post_id'))
        user_id = int(self.POST.get('user_id'))
        url_from = self.POST.get('url_from')

        user_inst = User.objects.get(id=user_id)
        blog_post_inst = Comment.objects.get(id=blog_post_id)

        try:
            blog_like_inst = LikePost.objects.get(blog_post=blog_post_inst, liked_by=user_inst)
        except LikePost.DoesNotExist:
            blog_like = LikePost(blog_post=blog_post_inst, liked_by=user_inst, like=True)
            blog_like.save()
            error = "You already liked this post"
            return error

        return redirect(url_from)
