from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def register_view(request):
	return HttpResponse('Register')

def login_view(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = UserLoginForm(request.POST)
		



def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    else:
        logout(request)
        return redirect('transactions:home')	