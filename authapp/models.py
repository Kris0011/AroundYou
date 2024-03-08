from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=10)
    role  = models.CharField(max_length=20 ,choices=[('customer', 'Customer'), ('service_provider', 'Service Provider')] , default='customer')
    img = models.FileField(upload_to='profile_pics', default='/v1/profile_pics/default.png')
    
class Customer(models.Model):
    user = models.OneToOneField(CustomUser , on_delete=models.CASCADE , primary_key=True)
    address = models.TextField(max_length=200)
    
class ServiceProvider(models.Model):
    user = models.OneToOneField(CustomUser , on_delete=models.CASCADE , primary_key=True)
    # services = models.ArrayField(models.CharField(max_length=100))
    # services_location = models.ArrayField(models.CharField(max_length=100))
    services = models.CharField(max_length=100)
    services_location = models.CharField(max_length=100)
    qualification = models.TextField()
    