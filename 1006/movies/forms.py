from django import forms
from .models import Movie

RATE_CHOICES = (
    ('first', '★'),         
    ('second', '★★'),
    ('third', '★★★'),
    ('fourth', '★★★★'),
    ('fifth', '★★★★★'),
)

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'summary', 'running_time', 'rate']
        labels = {'title': '제목', 'summary': '내용', 'running_time': '상영시간(분)', 'rate': '별점'}
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "summary": forms.Textarea(attrs={"class": "form-control"}),
            "running_time": forms.NumberInput(attrs={"class": "form-control"}),
            "rate": forms.Select(attrs={"class": "form-select"}),
        }