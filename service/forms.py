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
        
class FilterServices(forms.ModelForm):
    service_type =  forms.ChoiceField(choices=[('all', 'All'), ('plumber', 'Plumber'), ('electrician', 'Electrician'), ('carpenter', 'Carpenter'), ('tailor', 'Tailor'), ('cleaner', 'Cleaner')], widget=forms.Select(attrs={'class': 'select select-info w-full max-w-xs'}))
    
    service_location = forms.ChoiceField(choices=[('all', 'All'), ('ahmedabad', 'Ahmedabad'), ('vadodara', 'Vadodara'), ('nadiad', 'Nadiad') , ('rajkot' , 'Rajkot') , ('surat','Surat') ], widget=forms.Select(attrs={'class': 'select select-info w-full max-w-xs'}) )   
    
    class Meta:
        model = ServiceProvider
        fields = ['services', 'services_location']
    