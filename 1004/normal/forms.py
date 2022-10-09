from django import forms
from .models import Normal


class NormalForm(forms.ModelForm):
    class Meta:
        model = Normal
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.TextInput(attrs={"class": "form-control"}),
        }
