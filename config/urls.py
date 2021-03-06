"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# # Import views from app/main
# from app.main.views import homePage, loginPage

# # Import views from app/backend
# from app.backend.views import homePageAdmin, adminLoginProcess


# urlpatterns = [

# 	# FRONT PAGES
#     path('', homePage, name="home_page"),
# 	path('login/', loginPage, name="login_page"),
	
# 	# ADMIN PAGES
#     # path('admin/', admin.site.urls),
#     path('admin/', homePageAdmin, name='home_admin'),
#     path('admin/login_process', adminLoginProcess, name='login_process'),
    
# ]

# ------------------------------------
from django.contrib import admin
from django.urls import path, include

# app/backend
from app.backend.views import(
    adminLogin,
    adminHome,
    adminLoginProcess,
    adminLogoutProcess)

# app/main
from app.main.views import homePage

urlpatterns = [
    # main's app path
    path('', homePage, name='home'),

    # dashboard's app paths
    # path('admin/', admin.site.urls),
    path('admin/home', adminHome, name='admin_home'),
    path('admin/', adminLogin, name='admin_login'),
    path('admin/login_process', 
        adminLoginProcess, name='login_process'),
    path('admin/logout_process', 
        adminLogoutProcess, name='admin_logout_process'),
]
