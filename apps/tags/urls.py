from django.urls import path

from apps.tags.views import TagListView, TagDetailView, TagUpdateView, TagDeleteView


urlpatterns = [
    path('tags/', TagListView.as_view(), name="tag_list"),
    path('tags/<int:pk>', TagDetailView.as_view(), name="tag_detail"),
    path('update/<int:pk>', TagUpdateView.as_view(), name="tag_update"),
    path('delete-tag/<int:pk>', TagDeleteView.as_view(), name='tag_delete'),
]