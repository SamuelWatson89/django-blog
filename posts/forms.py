from django import forms
from .models import Post


class BlogPost(form.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'tag', 'published_date')