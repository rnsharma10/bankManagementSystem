from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm, CustomerForm, UserRegistrationForm
from django.contrib import messages
from .models import Customer
from .account_no_generate import accountGenerate

# Create your views here.
def register_view(request):
	if request.user.is_authenticated:
		return redirect('transactions:home')
	else:
		user_form = UserRegistrationForm(request.POST or None)
		customer_form = CustomerForm(request.POST or None)
		if user_form.is_valid() and customer_form.is_valid:
			user = user_form.save(commit=false)
			customer_details = customer_form.save(commit=False)
			password1 = user_form.cleaned_date.get('password1')
		context = {
			'title':'Create Bank Account',
			'user_form': user_form,
			'customer_form':customer_form
		}

		return render(request, 'accounts/register_form.html', context)

def login_view(request):
	if request.user.is_authenticated:
		return redirect('transactions:home')
	else:
		form = UserLoginForm(request.POST or None)
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
