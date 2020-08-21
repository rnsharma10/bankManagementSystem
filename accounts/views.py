from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm
from django.contrib import messages
from .models import Customer
# Create your views here.
def register_view(request):
	return HttpResponse('Register')

def login_view(request):
	if request.user.is_authenticated:
		return redirect('transactions:home')
	else:
		form = UserLoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('account_no')
			password = form.cleaned_data.get('password')
			user = authenticate(request, username=username, password=password)
			login(request, user)
			customer = Customer.objects.get(account_no = int(username))
			messages.success(request, 'Welcome, {}!' .format(customer.name))
			return redirect('transactions:home')
		context = {
			'form':form,
			'title':'Login'
		}
		return render(request, "accounts/form.html", context)


def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    else:
        logout(request)
        return redirect('transactions:home')
