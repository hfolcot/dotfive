from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
	"""
	New user registration form
	"""
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']
