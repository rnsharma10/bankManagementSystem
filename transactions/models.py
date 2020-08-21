from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from accounts.models import Customer

# Create your models here.
class Deposit(models.Model):
	customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
	amount = models.DecimalField(max_digits = 8, decimal_places=2)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.customer)+"->"+str(self.amount)

class Withdrawal(models.Model):
	customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
	amount = models.DecimalField(max_digits = 8, decimal_places=2)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.customer)+"->"+str(self.amount)