from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User


class MyForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required',
                             widget=forms.TextInput(attrs={"class": "form-text required  w-100"}))
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class": "form-text required  w-100"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-text required  w-100"}), max_length=32)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-text required  w-100"}), max_length=32)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class MyLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, "class": "form-text required  w-100"}))
    password = forms.CharField(label=("Password"), strip=False,
                               widget=forms.PasswordInput(attrs={"class": "form-text required  w-100"}))

    class Meta:
        model = User
        fields = ('username', 'password')




class MyPasswordResetConfirm(SetPasswordForm):
    error_messages = {
        'password_mismatch':("The two password fields didn't match."),
    }
    new_password1 = forms.CharField(
        label=("New password"),
        widget=forms.PasswordInput(attrs={"class": "form-text required  w-100"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "form-text required  w-100"}),
    )