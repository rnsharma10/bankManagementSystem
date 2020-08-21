from django.contrib import admin
from django.urls import path, include
from .views import depositView, withdrawalView, home, about, recordSheetView, export_excel
app_name = 'transactions'
urlpatterns = [
	path('', home, name='home'),
    path('about', about, name='about' ),
    path('deposit/', depositView, name='deposit'),
    path('withdrawal/', withdrawalView, name='withdrawal'),
    path('recordSheet/', recordSheetView, name='recordSheet'),
    path('export_excel/', export_excel, name='export_excel')
]
