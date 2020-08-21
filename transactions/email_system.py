from django.shortcuts import render
from banksystem.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
# Create your views here.
#DataFlair #Send Email

def creditMessage(account_no, amount, balance, email):
    subject = 'Amount Credited to bank account {}'.format(account_no)
    message = '{0} Rs. has been credited in your Bank Account {1}. \n Your balance is {2}'.format(amount, account_no, balance)
    recepient = str(email)
    send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)

def debitMessage(account_no, amount, balance, email):
    subject = 'Amount debited from bank account {}'.format(account_no)
    message = '{0} Rs. has been debited in your Bank Account {1}. \n Your balance is {2}'.format(amount, account_no, balance)
    recepient = str(email)
    send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)