from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import Customer
from transactions.models import Deposit, Withdrawal
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from .forms import DepositForm, WithdrawalForm
# Create your views here.
def home(request):
	if not request.user.is_authenticated:
		return render(request, "home.html")
	else:

		customer = Customer.objects.get(user=request.user)
		deposit = Deposit.objects.filter(customer=customer)
		deposit_total = deposit.aggregate(Sum('amount'))['amount__sum']
		withdrawal = Withdrawal.objects.filter(customer=customer)
		withdrawal_total = withdrawal.aggregate(Sum('amount'))['amount__sum']
		context = {
			'customer':customer,
			'deposit': deposit,
			'deposit_total':deposit_total,
			'withdrawal': withdrawal,
			'withdrawal_total': withdrawal_total
		}

		return render(request, 'transactions.html', context)

def about(request):
	return render(request, 'about.html')

@login_required
def depositView(request):
	context = {
		'title':'Deposit'
	}
	messages=[]
	if request.method == 'POST':
		form = DepositForm(request.POST)
		if form.is_valid():
			if int(request.POST['amount']) <= 10000000 and int(request.POST['amount']) > 0:
				deposit = form.save(commit=False)
				customer = get_object_or_404(Customer, user=request.user)
				deposit.customer = customer
				deposit.save()

				customer.balance += deposit.amount
				customer.save()
				return redirect('/')

			else:
				messages = ["Please enter a valid amount between 1 to 10000000"]
				context['messages'] = messages
				context['form'] = form
				return render(request, 'transactions/form.html', context)
	else:
		form = DepositForm()

		context['form'] = form
		context['balance'] = get_object_or_404(Customer, user=request.user).balance
		return render(request, "transactions/form.html", context)
					
				

@login_required
def withdrawalView(request):
	context = {
		'title':'Withdraw'
	}
	messages=[]
	if request.method == 'POST':
		form = WithdrawalForm(request.POST)
		if form.is_valid():
			if int(request.POST['amount']) <= 10000000 and int(request.POST['amount']) > 0:
				
				if withdraw.amount <= customer.balance:
					withdraw = form.save(commit=False)
					customer = get_object_or_404(Customer, user=request.user)
					withdraw.customer = customer
					withdraw.save()
					customer.balance -= withdraw.amount
					customer.save()
					return redirect('/')
				else:
					messages.append("You can not withdraw amount more than the balance in your account.")

			else:
				messages.append("Please enter a valid amount between 1 to 10000000.")
			context['messages'] = messages
			context['form'] = form
			return render(request, 'transactions/form.html', context)
	else:
		form = WithdrawalForm()

		context['form'] = form
		context['balance'] = get_object_or_404(Customer, user=request.user).balance
		return render(request, "transactions/form.html", context)
