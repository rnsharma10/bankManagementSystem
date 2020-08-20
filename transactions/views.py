from django.shortcuts import render
from accounts.models import Customer
# Create your views here.
def home(request, pk):
	if not request.user.is_authenticated:
		return render(request, "home.html")
	else:

		customer = Customer.object.get(id=pk)
		
		context = {
			'customer':customer
		}
		return render(request, 'transactions.html', context)

def about(request):
	return render(request, 'about.html')


