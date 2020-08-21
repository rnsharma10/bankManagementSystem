import django_filters
from django_filters import DateFilter
from .models import Deposit, Withdrawal
from accounts.models import Customer


class DepositTransactionFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name='timestamp', lookup_expr='gte', label='From')
	end_date = DateFilter(field_name='timestamp', lookup_expr='lte', label='To')
	class Meta:
		model = Deposit
		fields = ['customer']

class WithdrawalTransactionFilter(django_filters.FilterSet):
	class Meta:
		model = Withdrawal
		fields = ['customer']