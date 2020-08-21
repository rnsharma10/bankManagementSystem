from .models import Customer
from django.db.models import Max
def accountGenerate():
	largest = Customer.objects.all().aggregate(
		Max('account_no')
	)['account_no__max']
	if largest:
		largest+=1
	else:
		largest = 10000000

	return str(largest)