from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth import authenticate , login ,logout

from authapp.forms import CustomerForm, ServiceProviderForm, UserLoginForm , UserCreationForm
from authapp.models import Customer, ServiceProvider
from service.models import ServiceRequest

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return render(request , 'home.html' , context = { 'isLoggedin' : True , 'user' : request.user})
    return render(request , 'home.html' , context = { 'isLoggedin' : False , 'user' : None})

def register_request(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        # print(form)

        if form.is_valid():
            # print(form.cleaned_data)
            user = form.save()
            login(request , user)
            
            messages.success(request , "Registration successful , Now set more details in profile.")
            
            return redirect('/set_profile/' , context = { 'user' : user})
        else:
            # print(form.errors)
            messages.error(request , "Unsuccessful registration. Invalid information")
    
    form = UserCreationForm()
    # print(customer_form)
    # print(serviceprovider_form)
    return render(request , 'auth/register.html' , context={'register_form': form })

def login_request(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username , password=password)
            if user is not None:
                login(request , user)
                print(user.username)
                messages.success(request , f"You are now logged in as {username}")
                return redirect('/' ,context = { 'user' : user})
            else:
                messages.error(request , "Invalid username or password")
        else:
            messages.error(request , "Invalid username or password")
    
    form = UserLoginForm()
    # print(form)
    return render(request , 'auth/login.html' , context={'login_form': form })
    
def logout_request(request):
    logout(request)
    messages.info(request , "You have successfully logged out.")
    return redirect('/')

def set_profile(request):
    user = request.user
    if user.is_authenticated:
        if user.role == 'service_provider':
            return users/set_serviceprovider_details(request)
        elif user.role == 'customer':
            return set_customer_details(request)
        else:
            messages.error(request , "Invalid role")
            return redirect('/' , context = { 'user' : user})
    else:
        messages.error(request , "You are not logged in")
        return redirect('/login/')
    


def set_customer_details(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user
            customer.save()
            messages.success(request , "Customer details saved successfully")
            return redirect('/' , context = { 'user' : request.user })
        else:
            messages.error(request , "Unsuccessful registration. Invalid information")
    
    form = CustomerForm()
    return render(request , 'users/set_customer_details.html' , context={'customer_form': form  , 'isLoggedin' : True , 'user' : request.user , 'role' : 'customer'})

def set_serviceprovider_details(request):
    if request.method == "POST":
        form = ServiceProviderForm(request.POST)
        if form.is_valid():
            serviceprovider = form.save(commit=False)
            serviceprovider.user = request.user
            serviceprovider.save()
            messages.success(request , "Service provider details saved successfully")
            return redirect('/' , context = { 'user' : request.user , 'isLoggedin' : True})
        else:
            messages.error(request , "Unsuccessful registration. Invalid information")
    
    form = ServiceProviderForm()
    return render(request , 'users/set_serviceprovider_details.html' , context={'serviceprovider_form': form  , 'isLoggedin' : True , 'user' : request.user , 'role' : 'service_provider'})

def profile(request):
    user  = request.user

    if user.is_authenticated:
        if user.role == 'service_provider':
            sp_user = ServiceProvider.objects.get(user = user)
            services = sp_user.services.split(',')
            # print(services)
            
            return render(request , 'serviceprovider_profile.html' , context = { 'user' : user , 'serviceprovider' : sp_user , 'services' : services , 'isLoggedin' : True})
        elif user.role == 'customer':
            customer = Customer.objects.get(user = user)
            services_requests  = ServiceRequest.objects.filter(customer = customer)
            return render(request , 'users/customer_profile.html' , context = { 'user' : user , 'customer' : customer , 'isLoggedin' : True , 'service_requests' : services_requests})
        else:
            messages.error(request , "Invalid role")
            return redirect('/' , context = { 'user' : user})
    else :
        messages.error(request , "You are not logged in")
    return redirect('/login/')
