from django import forms
from apps.tags.models import Tag


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['text',]

