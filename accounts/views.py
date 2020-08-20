from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def register_view(request):
	return HttpResponse('Register')

def login_view(request):
	return HttpResponse('login')

def logout_view(request):
	return HttpResponse('logout')