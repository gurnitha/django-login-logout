# app/main/views.py
from django.shortcuts import render

# Create your views here.
def homePage(request):
	return render(request, 'main/home.html')

def loginPage(request):
	return render(request, 'main/login.html')