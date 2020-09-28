from django import forms

class RegisterForm(forms.Form):
    user_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'required': True, 'name': 'register_usr', 'id': 'register_usr', 'minlength':4}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'required': True, 'name': 'register_email', 'id': 'register_email'}))
    pwd = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'required': True, 'name': 'register_pwd', 'id': 'register_pwd', 'minlength': 8}))

class LoginForm(forms.Form):
    user_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'required': True, 'name': 'login_usr', 'id': 'login_usr','minlength':4}))
    pwd = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'required': True, 'name': 'login_pwd', 'id': 'login_pwd', 'minlength': 8}))
    remember = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'placeholder': 'Password', 'required': True, 'name': 'login_pwd', 'id': 'login_pwd', 'minlength': 8}))

class PasswordChange(forms.Form):
    new_pwd = forms.CharField(label='New Password: ', max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control w-25', 'placeholder': 'Password', 'required': True, 'name': 'pwd-change', 'id': 'pwd_change', 'minlength': 8}))
    confirm_pwd = forms.CharField(label='Confirm Password: ', max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control w-25', 'placeholder': 'Password', 'required': True, 'name': 'pwd_confirm', 'id': 'pwd_confirm', 'minlength': 8}))

class PasswordReset(forms.Form):
    user_pwd_reset = forms.CharField(label='Username: ', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control w-25', 'placeholder': 'Username', 'required': True, 'name': 'reset_usr', 'id': 'reset_usr', 'minlength':4}))
    email_pwd_reset = forms.EmailField(label='Email address: ', widget=forms.EmailInput(attrs={'class': 'form-control w-25', 'placeholder': 'Email', 'required': True, 'name': 'reset_email', 'id': 'reset_email'}))