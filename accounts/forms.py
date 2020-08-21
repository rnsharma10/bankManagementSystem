from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import Customer


class UserRegistrationForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['email'].required = True
	class Meta:
		model = User
		fields = [
			'email',
			'password1',
			'password2'
		]

class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = [
			'name',
			'gender',
			'phone'
		]
class UserLoginForm(forms.Form):
	account_no = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get('account_no')
		password = self.cleaned_data.get('password')

		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError('this user does not exist')
			if not user.check_password(password):
				raise forms.ValidationError('Incorrect Password')
			return super(UserLoginForm, self).clean(*args, **kwargs)