from django.forms import ModelForm, widgets
from django import forms
from .models import Post

# Create a POST form


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'title', 'content', 'status')
        labels = {
            'name': '',
            'title': '',
            'content': '',
        }

        STATUS = [(0,'Draft'),(1,'Publish')]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),

            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title'}),

            'content': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is your canvas of imagination'}),

            'status': forms.Select(choices=STATUS),
        }
