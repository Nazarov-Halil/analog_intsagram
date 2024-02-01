from django.contrib import admin

from apps.posts.models import Post, Images


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['description']


admin.site.register(Images)
