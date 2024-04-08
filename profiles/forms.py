from django import forms
from .models import Profile, User
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.contrib.auth import authenticate, get_user_model



class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Имя')
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, request = None, *args, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = authenticate(self.request, username=username, password=password)
        if not user:
            raise ValidationError('Неправильный ЛОГИН')
        return self.cleaned_data





class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, label='Имя')
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        User = get_user_model()
        if User.objects.filter(username=username).exists():
            raise ValidationError('Такой пользователь уже есть')
        else:
            return username

    def clean(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise ValidationError('Пароль не совпадает')
        else:
            return password
