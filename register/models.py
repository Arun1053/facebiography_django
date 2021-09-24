from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.


class Reg_User(models.Model):
    email = models.EmailField(unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    age = models.IntegerField(blank=True)
    marital_status = models.CharField(max_length=10, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    contact = models.IntegerField(blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=30, blank=True)
    zipcode = models.IntegerField(blank=True)



