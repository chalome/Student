from django import forms
from account.models import CustomUser
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import get_user_model

class LoginForm(AuthenticationForm):
	username=forms.CharField(max_length=128,label='username')
	password=forms.CharField(max_length=255,label='password',widget=forms.PasswordInput)

class SignUpForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model=CustomUser
		fields=['username','email','profile_photo']

