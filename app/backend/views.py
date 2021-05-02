# app/backend/views.py
# from django.shortcuts import render
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from django.http import HttpResponseRedirect
# from django.urls import reverse

# # Create your views here.

# def homePageAdmin(request):
# 	return render(request, 'backend/home.html')


# #adminLogin
# def adminLogin(request):
	
# 	# Get the input (username and password) from the login form
# 	username=request.POST.get('username')
# 	password=request.POST.get('password')

# 	# Authenticate user input(credentials)
# 	user=authenticate(
# 		request=request,username=username,password=password)

# 	# If user exist in the database
# 	if user is not None:
# 		login(request=request, user=user)
# 		return HttpResponseRedirect(reverse('home_admin'))

# 	# If user is not exist in the database
# 	else:
# 		messages.error(request, 'Invalid login detail!')
# 		return HttpResponseRedirect(reverse('login_page'))

# def adminLoginProcess(request):
# 	return render(request, 'backend/login_process.html')

# START FROM ZERO AGAIN

# app/dashboard/views.py
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def adminLogin(request):
	return render(request, 'backend/login.html')

def adminHome(request):
	return render(request, 'backend/home.html')

def adminLoginProcess(request):
	return render(request, 'backend/login_process.html')

def adminLoginProcess(request):
	# Get input from the login form
	username=request.POST.get('username')
	password=request.POST.get('password')

	# Authenticate user credentials
	user=authenticate(
		request=request,
		username=username,
		password=password)

	# If user exist
	if user is not None:
		login(request=request, user=user)
		return HttpResponseRedirect(reverse('admin_home'))
	# If user not exist
	else:
		messages.error(
			request, 'Login error! Invalid login detail!')
		return HttpResponseRedirect(reverse('admin_login'))

def adminLogoutProcess(request):
	logout(request)
	messages.success(request, 'Logged out successfully!')
	return HttpResponseRedirect(reverse('admin_login'))
