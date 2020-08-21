from .models import Customer
def accountGenerate():
	largest = Customer.objects.all().aggregate(
		Max('account_no')
	)['account_no__max']
	if largest:
		largest+=1
	else:
		largest = 10000000
		
	return largest