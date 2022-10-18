from django import forms
from django.forms import ClearableFileInput
from .models import Article, Photo

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'

class PhotoForm(forms.ModelForm):
  
    class Meta:
        model = Photo
        fields = ('image', )
        widgets = {
            'image': ClearableFileInput(attrs={'multiple': True}),
        }