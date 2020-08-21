from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class UserRegistrationForm(UserCreatioForm):
	class Meta:
		model = User
		fields = [
			'email',
			'phone',
			'password1'
			'password2'
		]

class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = [
			'name',
			'gender',

		]

class UserLoginForm(forms.Form):
	account_no = forms.IntegerField(label="Account Number")
	password = forms.CharField(widget = forms.PasswordInput)
	