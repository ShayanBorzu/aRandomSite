from django import forms
from blogApp.models import Comment, NewsLetter
from captcha.fields import CaptchaField


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["full_name", "email", "text", "post"]


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = [
            "email",
        ]
