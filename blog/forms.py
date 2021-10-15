from django.forms import ModelForm
from .models import Post

# Create a POST form


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'content', 'status')