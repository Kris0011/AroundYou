from django.db import models
from authapp.models import Customer , CustomUser , ServiceProvider

# Create your models here.

class ServiceRequest(models.Model):
    req_id = models.AutoField(primary_key=True)
    customer = models.OneToOneField(Customer , on_delete=models.CASCADE)
    service_provider = models.OneToOneField(ServiceProvider  , on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    request_status = models.CharField(max_length=20 , choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected') , ('completed' , 'Completed')] , default='pending')

    