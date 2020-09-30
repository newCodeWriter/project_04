from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from django.core.exceptions import ValidationError

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'required': True, 'name': 'register_usr', 'id': 'register_usr', 'minlength':4}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'required': True, 'name': 'register_email', 'id': 'register_email'}))
    pwd = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'required': True, 'name': 'register_pwd', 'id': 'register_pwd', 'minlength': 8}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists.")

        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email already belongs to an account.")

        return email

    def save(self, commit=True):
        user = User.objects.create_user(
                self.cleaned_data['username'],
                self.cleaned_data['email'],
                self.cleaned_data['pwd']
        )
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'required': True, 'name': 'login_usr', 'id': 'login_usr','minlength':4}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'required': True, 'name': 'login_pwd', 'id': 'login_pwd', 'minlength': 8}))
    remember = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

        
class PasswordChange(PasswordChangeForm):
    old_password =  forms.CharField(label='Old Password: ', max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control w-25', 'name': 'old-pwd', 'id': 'old-pwd', 'minlength': 8}))
    new_password1 = forms.CharField(label='New Password: ', max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control w-25', 'name': 'pwd-change', 'id': 'pwd_change', 'minlength': 8}))
    new_password2 = forms.CharField(label='Confirm Password: ', max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control w-25', 'name': 'pwd_confirm', 'id': 'pwd_confirm', 'minlength': 8}))

class PasswordReset(forms.Form):
    user_pwd_reset = forms.CharField(label='Username: ', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control w-25', 'placeholder': 'Username', 'required': True, 'name': 'reset_usr', 'id': 'reset_usr', 'minlength':4}))
    email_pwd_reset = forms.EmailField(label='Email address: ', widget=forms.EmailInput(attrs={'class': 'form-control w-25', 'placeholder': 'Email', 'required': True, 'name': 'reset_email', 'id': 'reset_email'}))