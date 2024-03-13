from django import forms
from .models import CustomUser , ServiceProvider , Customer
from django.contrib.auth.forms import UserCreationForm

class UserCreationForm(UserCreationForm):
    role_choices = [('customer', 'Customer'), ('service_provider', 'Service Provider')]
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input input-bordered w-full max-w-xs', 'placeholder': 'Enter your username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input input-bordered w-full max-w-xs', 'placeholder': 'Enter your email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input input-bordered w-full max-w-xs', 'placeholder': 'Enter your first name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input input-bordered w-full max-w-xs', 'placeholder': 'Enter your last name'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'input input-bordered w-full max-w-xs', 'placeholder': 'Enter your phone number'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input input-bordered w-full max-w-xs', 'placeholder': 'Enter your password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input input-bordered w-full max-w-xs', 'placeholder': 'Confirm your password'}))
    role = forms.ChoiceField(choices=role_choices, widget=forms.Select(attrs={'class': 'input input-bordered w-full max-w-xs'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'phone', 'password1', 'password2', 'role']
        
        
        
class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input input-bordered w-full max-w-xs' , 'placeholder': 'Enter your username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input input-bordered w-full max-w-xs' , 'placeholder': 'Enter your password'}))
    
class ServiceProviderForm(forms.ModelForm):
    services = forms.CharField(widget=forms.TextInput(attrs={'class': 'input input-bordered w-full max-w-xs' , 'placeholder': 'Enter your Services'}))
    services_location = forms.CharField(widget=forms.TextInput(attrs={'class': 'input input-bordered w-full max-w-xs' , 'placeholder': 'Enter your service locations'}))
    qualification = forms.CharField(widget=forms.TextInput(attrs={'class': 'textarea textarea-bordered h-24 w-full', 'placeholder': 'Enter your qualification'}))
    class Meta:
        model = ServiceProvider
        fields = ['services', 'services_location', 'qualification']
        
class CustomerForm(forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'textarea textarea-bordered h-24 w-full', 'placeholder': 'Enter your address'}))
    
    class Meta:
        model = Customer
        fields = ['address']

class edit_Common(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input input-bordered w-full max-w-xs', 'placeholder': 'Enter your email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input input-bordered w-full max-w-xs', 'placeholder': 'Enter your first name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input input-bordered w-full max-w-xs', 'placeholder': 'Enter your last name'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'input input-bordered w-full max-w-xs', 'placeholder': 'Enter your phone number'}))

    class Meta:
        model=CustomUser
        fields=["email","first_name","last_name","phone"]

class edit_CustomerForm(forms.ModelForm):
   address = forms.CharField(widget=forms.TextInput(attrs={'class': 'textarea textarea-bordered h-24 w-full', 'placeholder': 'Enter your address'}))

   class Meta:
       model=Customer
       fields=["address"]

class edit_ServiceProviderForm(forms.ModelForm):
    services = forms.CharField(widget=forms.TextInput(attrs={'class': 'input input-bordered w-full max-w-xs' , 'placeholder': 'Enter your Services'}))
    services_location = forms.CharField(widget=forms.TextInput(attrs={'class': 'input input-bordered w-full max-w-xs' , 'placeholder': 'Enter your service locations'}))
    qualification = forms.CharField(widget=forms.TextInput(attrs={'class': 'textarea textarea-bordered h-24 w-full', 'placeholder': 'Enter your qualification'}))

    class Meta:
        model=ServiceProvider
        fields=["services","services_location","qualification"]

