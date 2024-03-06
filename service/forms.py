from django import forms
from .models import ServiceRequest
from authapp.models import *

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['description']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control' , 'placeholder': 'Enter your request description'})
        }
        labels = {
            'description': 'Description'
        }
    