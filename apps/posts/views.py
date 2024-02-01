from django.forms import inlineformset_factory
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)

from apps.posts.models import Post, Images
from apps.posts.forms import PostCreateForm
from django.urls import reverse_lazy

from apps.posts.forms import Images
from apps.posts.forms import ImagesForm


class PostListView(ListView):
    model = Post
    template_name = 'index.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'
    pk_url_kwarg = 'pk'


class PostDeleteView(DeleteView):
    model = Post
    pk_url_kwarg = 'pk'
    template_name = 'delete.html'
    success_url = '/'


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'create_post.html'
    success_url = '/'
    extra = 3

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.object = None

    def get_context_data(self, instance=None, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            data['formset'] = inlineformset_factory(Post, Images, form=ImagesForm, extra=self.extra)(
                self.request.POST, self.request.FILES, instance=self.object
            )
        else:
            data['formset'] = inlineformset_factory(Post, Images, form=ImagesForm, extra=self.extra)()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        if formset.is_valid():
            form.instance.author = self.request.user
            self.object = form.save()
            formset.instance = self.object
            formset.save()
        return super().form_valid()

    class PostUpdateView(UpdateView):
        model = Post
        form_class = PostCreateForm
        template_name = '/'
        success_url = '/'

        def form_valid(self, form):
            post = form.save(commit=False)
            post.save()
            return super().form_valid(form)
