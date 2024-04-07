from django import forms
from .models import Profile, User
from django.core.exceptions import ValidationError
from django.http import HttpResponse

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Имя')
    password = forms.CharField(widget=forms.PasswordInput)


    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            return username
        else:
            print('NOUSERNAME:', username)
            raise ValidationError('Неправильный ЛОГИН')



class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, label='Имя')
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)