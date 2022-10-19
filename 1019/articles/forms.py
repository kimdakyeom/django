from django import forms
from django.forms import ClearableFileInput
from .models import Article, Photo, Comment

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'content', 'thumbnail')

class PhotoForm(forms.ModelForm):
  
    class Meta:
        model = Photo
        fields = ('image', )
        widgets = {
            'image': ClearableFileInput(attrs={'multiple': True}),
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)
        labels = {
            'content': '',
        }