from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm, CustomerForm, UserRegistrationForm
from django.contrib import messages
from .models import Customer
from .account_no_generate import accountGenerate
from django.contrib.auth.models import User

# Create your views here.
def register_view(request):
    if request.user.is_authenticated:
        return redirect('transactions:home')
    else:
        user_form = UserRegistrationForm(request.POST or None)
        customer_form = CustomerForm(request.POST or None)

        if user_form.is_valid() and customer_form.is_valid():

            email = user_form.cleaned_data.get('email')
            password1 = user_form.cleaned_data.get('password1')

            username = accountGenerate()

            user = User.objects.create_user(username=username, email=email, password=password1)
            customer = Customer(
                user=user, 
                name=customer_form.cleaned_data.get('name'),
                account_no=int(username), 
                gender=customer_form.cleaned_data.get('gender'),
                email=email, 
                phone=customer_form.cleaned_data.get('phone'),
            )
            customer.save()
            login(request, user)
            messages.add_message(request, messages.SUCCESS,
                '''Hi, {}! Your account has been opened in Private bank. Your Account number is {}. 
                Please use this for login next time.'''.format(
                customer.name, customer.account_no)
            )
            for message in messages.get_messages(request):
                print(message.tags)
            return redirect("transactions:home")
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
            messages.add_message(request, messages.SUCCESS, 'Welcome, {}!'.format(customer.name))
            
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
