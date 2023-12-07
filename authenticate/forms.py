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

class SignUpForm(forms.ModelForm):
    username = forms.CharField(
        max_length=32,
        help_text='Required. 32 characters or less. Letters and numbers only.',
        label = 'Username:',
        widget = forms.TextInput(attrs=(
            {'class': 'form-control',
            'placeholder': 'Enter your username.'}
        ))
    )

    email = forms.EmailField(
        max_length=254,
        help_text='Required. Enter a valid email.',
        label = 'Email:',
        widget = forms.TextInput(attrs=(
            {'class': 'form-control',
            'placeholder': 'Enter your email.'}
        ))
    )

    email2 = forms.EmailField(
        max_length=254,
        help_text='Required. Enter a valid email.',
        label = 'Confirm your email:',
        widget = forms.TextInput(attrs=(
            {'class': 'form-control',
            'placeholder': 'Confirm your email.'}
        ))
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        email2 = cleaned_data.get('email2')

        if email != email2:
            raise forms.ValidationError(
                "The two emails must be the same. Please try again."
            )

    class Meta:
        model = User
        fields = ('username', 'email', 'email2')