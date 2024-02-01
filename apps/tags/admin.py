from django.contrib import admin

from apps.tags.models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['text']
    search_fields = ['text']
