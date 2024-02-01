from django.urls import path
from apps.likes.views import AddLikeView

urlpatterns = [
    path('like_post/', AddLikeView.as_view(), name='Like_Post'),
]
