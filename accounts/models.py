from django.db import models
from django.contrib.auth.models import  AbstractUser
from django import forms
# Create your models here.

class CustomUser(AbstractUser):
    phone_number= models.CharField('phone number',max_length=15,blank=True,null=True,)
    age = models.PositiveSmallIntegerField(blank=True,null=True)
    
