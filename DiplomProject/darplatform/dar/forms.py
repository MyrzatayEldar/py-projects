from django import forms
from .models import *


class CommentForm(forms.Form):
    name = forms.CharField(label='Your name.')
    comment = forms.CharField(label='Your comment.')
    date = forms.DateTimeField()


class LoginForm(forms.Form):
    login = forms.CharField(label='Введите свой логин.')
    password = forms.CharField(widget=forms.PasswordInput(), label='Введите свой пароль.')

    class Meta:
        model = ProfileLoginAndPassword


class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='Введите свое имя.')
    last_name = forms.CharField(label='Введите свое отчество.')
    surname = forms.CharField(label='Введите свою фамилию.')
    birthday = forms.DateField()
    email = forms.EmailField()

    class Meta:
        model = ProfileInfo


