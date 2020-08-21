from django.http import HttpResponse
from django.shortcuts import redirect

def admin_only(view_func):
	def wrapper_func(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'customer':
			return redirect('transaction:home')

		elif group == 'admin':
			return view_func(request, *args, **kwargs)
		else:
			print(group)
			return HttpResponse('Not authorized')
	return wrapper_func