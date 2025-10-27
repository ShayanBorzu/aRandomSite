from django import forms
from blogApp.models import Comment, NewsLetter


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['full_name', 'email', 'website', 'text', 'post']
        
class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ['email',]