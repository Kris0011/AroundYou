from django.db import models
from authapp.models import Customer, CustomUser, ServiceProvider

class ServiceRequest(models.Model):
    req_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(max_length=1000)
    request_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected'), ('completed', 'Completed')], default='pending')
