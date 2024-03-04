from django import forms
from .models import ServiceProvider , Customer , CustomUser
from django.contrib.auth.forms import UserCreationForm

class UserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username' , 'email' , 'name', 'phone'  , 'password1' , 'password2' , 'is_serviceprovider' , 'is_customer' , 'is_admin']
        
        
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
