from django import forms
from mainApp.models import Contact
from captcha.fields import CaptchaField


class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'phone_number', 'subject', 'message']