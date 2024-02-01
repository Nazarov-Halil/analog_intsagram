from django.urls import path
from apps.comments.views import (
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)

urlpatterns = [
    path('comment_create/<int:pk>/', CommentCreateView.as_view(), name='comment-create'),
    path('comment_update/<int:pk>/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment_delete/<int:pk>', CommentDeleteView.as_view(), name='comment-delete')
]