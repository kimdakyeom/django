from django import forms
from .models import Review, Comment, ReComment

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content', 'movie_title', 'grade', )
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        labels = {
            'content': '',
        }

class ReCommentForm(forms.ModelForm):
    class Meta:
        model = ReComment
        fields = ('body',)
        labels = {
            'body': '',
        }