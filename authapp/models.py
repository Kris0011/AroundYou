from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    is_serviceprovider = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
class Customer(models.Model):
    user = models.OneToOneField(CustomUser , on_delete=models.CASCADE , primary_key=True)
    address = models.CharField(max_length=100)
    
class ServiceProvider(models.Model):
    user = models.OneToOneField(CustomUser , on_delete=models.CASCADE , primary_key=True)
    services = models.CharField(max_length=100)
    services_location = models.CharField(max_length=100)
    qualification = models.TextField()
    