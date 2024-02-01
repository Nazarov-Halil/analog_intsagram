from django.contrib import admin
from apps.likes.models import LikeComment, LikePost

admin.site.register(LikeComment)
admin.site.register(LikePost)
