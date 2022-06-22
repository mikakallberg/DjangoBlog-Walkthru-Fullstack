from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        # trailing comma is important otherwise python
        # interprets body as a string intead of a tupple
