from django import forms
from .models import Post
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'description', 'category', 'post_image', 'post_published')