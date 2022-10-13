from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Article

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email',)
        help_texts = {
            'username': None,
        }


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'content']