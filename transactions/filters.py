import django_filters
from django_filters import DateFilter
from .models import Deposit, Withdrawal
from accounts.models import Customer
from django.forms.widgets import TextInput

class DepositTransactionFilter(django_filters.FilterSet):
	start_date = DateFilter(
		field_name='timestamp', 
		lookup_expr='gte', 
		label='From', 
		widget=TextInput(attrs={'placeholder': 'MM/DD/YYYY'})
	)

	end_date = DateFilter(
		field_name='timestamp', 
		lookup_expr='lte', 
		label='To', 
		widget=TextInput(attrs={'placeholder': 'MM/DD/YYYY'})
	)
	class Meta:
		model = Deposit
		exclude = ['customer', 'amount', 'timestamp']

class WithdrawalTransactionFilter(django_filters.FilterSet):
	start_date = DateFilter(
		field_name='timestamp', 
		lookup_expr='gte', 
		label='From', 
		widget=TextInput(attrs={'placeholder': 'MM/DD/YYYY'})
	)
	
	end_date = DateFilter(
		field_name='timestamp', 
		lookup_expr='lte', 
		label='To', 
		widget=TextInput(attrs={'placeholder': 'MM/DD/YYYY'})
	)
	class Meta:
		model = Withdrawal
		exclude = ['customer', 'amount', 'timestamp']