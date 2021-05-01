# app/backend/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# CustomUser model
class CustomUser(AbstractUser):

	"""There will be 4 type of users: Admin, Staff, Merchant, Customer"""
	user_type_choices=(
		(2,"Admin"),(2,"Staff"),
		(3,"Merchant"),(4,"Customer"))
	
	user_type=models.CharField(
		choices=user_type_choices,
		default=1, max_length=225 )