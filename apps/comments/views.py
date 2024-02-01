from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView
)

from apps.comments.models import Comment
from apps.comments.forms import CommentForm


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'comments/delete.html'
    success_url = '/'


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments/create.html'
    success_url = '/'

    context_object_name = 'comment'




class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments/update.html'
    success_url = '/'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return super().form_valid(form)
