from django.urls import path

from apps.posts.views import PostListView, PostDetailView, PostDeleteView, PostCreateView


urlpatterns = [
    path('', PostListView.as_view(), name="list_post"),
    path('post/<int:pk>', PostDetailView.as_view(), name="detail_post"),
    path('delete/<int:pk>', PostDeleteView.as_view(), name="delete_post"),
    path('create/', PostCreateView.as_view(), name="create_post"),
]