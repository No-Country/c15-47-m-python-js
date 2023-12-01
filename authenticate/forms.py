from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User

class FormLogin(AuthenticationForm):
    email = forms.CharField(
        max_length=50,
        required=True,
        label='Email',
        error_messages={'required': 'Email is mandatory'},
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )
    password = forms.CharField(
        max_length=16,
        required=True,
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
        error_messages={'required': 'Password is mandatory'}
    )

    class Meta:
        model = User