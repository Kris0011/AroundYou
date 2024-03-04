from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate , login

from authapp.forms import UserLoginForm

# Create your views here.

def home(request):
    return render(request , 'home.html')

def register_request(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request , "Registration successful")
            return redirect('')
        else:
            messages.error(request , "Unsuccessful registration. Invalid information")
    
    form = UserCreationForm()
    print(form)
    return render(request , 'register.html' , context={'register_form': form})

def login_request(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username , password=password)
            if user is not None:
                login(request , user)
                messages.info(request , f"You are now logged in as {username}")
                return redirect('')
            else:
                messages.error(request , "Invalid username or password")
        else:
            messages.error(request , "Invalid username or password")
    
    form = UserLoginForm()
    # print(form)
    return render(request , 'login.html' , context={'login_form': form})
        
        