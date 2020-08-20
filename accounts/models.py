from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length = 200, null=True)
	account_no = models.PositiveIntegerField(
		unique=True, 
		validators=[MinValueValidator(10000000),MaxValueValidator(99999999)]
	)
	balance = models.DecimalField(default=10,max_digits=8,decimal_places=2)
	GENDER_CHOICE = (
		('M', 'Male'),
		('F', 'Female')
	)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
	phone = models.IntegerField(unique=True, blank=True, null=True)
	email = models.EmailField(unique=True, null=False, blank=False)
	date_create = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return str(str(self.account_no)+"-"+self.name)