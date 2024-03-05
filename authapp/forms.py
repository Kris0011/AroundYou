from django import forms
from .models import CustomUser , ServiceProvider , Customer
from django.contrib.auth.forms import UserCreationForm

class UserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'phone', 'password1', 'password2', 'role']
        role = forms.ChoiceField(choices=[('customer', 'Customer'), ('service_provider', 'Service Provider')])
        
        
        
class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Enter your username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control' , 'placeholder': 'Enter your password'}))
    
class ServiceProviderForm(forms.ModelForm):
    class Meta:
        model = ServiceProvider
        fields = ['services', 'services_location', 'qualification']
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['address']
