from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)
from apps.tags.models import Tag
from apps.tags.forms import TagForm


class TagListView(ListView):

    model = Tag
    template_name = 'tags/index.html'


class TagDetailView(DetailView):

    model = Tag
    template_name = 'tags/detail.html'
    pk_url_kwarg = 'pk'


class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'tags/delete.html'
    success_url = '/'


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'tags/update.html'
    success_url = '/'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return super().form_valid(form)