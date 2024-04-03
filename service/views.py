from django.shortcuts import redirect, render
from authapp.models import ServiceProvider , CustomUser , Customer
from django.contrib import messages

from service.forms import FilterServices, ServiceRequestForm
from service.models import ServiceRequest


# Create your views here.

def index(request):
    if request.method == 'POST':
        filter_form = FilterServices(request.POST)
        if filter_form.is_valid:
            print(filter_form)    #i don't know why without this it was not working !!!!!
            service_type = filter_form.cleaned_data['service_type']
            service_location = filter_form.cleaned_data['service_location']
            if service_type == 'all' and service_location == 'all':
                service_providers = ServiceProvider.objects.all()
                filter_form = FilterServices()  
            elif service_type == 'all':
                service_providers_temp = ServiceProvider.objects.all()
                service_providers = []
                for sp in service_providers_temp:
                    if sp.services_location.upper().find(service_location.upper()) != -1:
                        service_providers.append(sp)
                filter_form = FilterServices()
                filter_form.fields['service_location'].initial = service_location      
            elif service_location == 'all':
                service_providers_temp = ServiceProvider.objects.all()
                service_providers = []
                for sp in service_providers_temp:
                    if sp.services.upper().find(service_type.upper()) != -1:
                        service_providers.append(sp)
                filter_form = FilterServices()
                filter_form.fields['service_type'].initial = service_type            
            else:
                service_providers_temp = ServiceProvider.objects.all()
                service_providers = []
                for sp in service_providers_temp:
                    if sp.services.upper().find(service_type.upper()) != -1 and sp.services_location.upper().find(service_location.upper()) != -1:
                        service_providers.append(sp)
                filter_form = FilterServices()
                filter_form.fields['service_location'].initial = service_location
                filter_form.fields['service_type'].initial = service_type

            return render(request , 'service/services.html' , {'service_providers':service_providers , 'isLoggedin':request.user.is_authenticated , 'user':request.user , 'filter_form':filter_form})  
        
    filter_form = FilterServices()    
    service_providers = ServiceProvider.objects.all()
    return render(request , 'service/services.html' , {'service_providers':service_providers , 'isLoggedin':request.user.is_authenticated , 'user':request.user , 'filter_form':filter_form})


def request_service(request , sp_id):
    # print("inside the request function")
    if request.user.is_authenticated:
        custom_user  = CustomUser.objects.get(id = sp_id)
        if custom_user.role != 'service_provider':
            messages.error(request , "Service provider not found")
            return redirect('/')
        sp_user = ServiceProvider.objects.get(user = custom_user) 
        if sp_user is None:
            messages.error(request , "Service provider not found")
            return redirect('/')
        if request.method == 'POST':
            s_request_form = ServiceRequestForm(request.POST)
            if s_request_form.is_valid():
                book = s_request_form.save(commit=False)
                book.customer = Customer.objects.get(user = request.user)
                book.service_provider = sp_user
                book.save()
                messages.success(request , "Booking successful")
                return redirect('/' , context = { 'user' : request.user})
            

        s_request_form = ServiceRequestForm()
        return render(request , 'service/service_request.html' , {'s_request_form':s_request_form , 'isLoggedin':request.user.is_authenticated , 'user':request.user , 'sp_user' : sp_user})
    
    else:
        messages.error(request , "Please login to request service")
        return redirect('/service/allservices/')


def complete_service(request , req_id):
    user = request.user
    if user.is_authenticated:
        service_request = ServiceRequest.objects.get(req_id = req_id)
        service_request.request_status = 'completed'
        service_request.save()
        messages.success(request , "Service request completed successfully")
        return redirect('/profile/' , context = { 'user' : user})
    else:
        messages.error(request , "You are not logged in")
        return redirect('/login/')
        
        
def accept_service(request , req_id):
    user = request.user
    if user.is_authenticated:
        service_request = ServiceRequest.objects.get(req_id = req_id)
        service_request.request_status = 'accepted'
        service_request.save()
        messages.success(request , "Service request accepted successfully")
        return redirect('myservices' , context = { 'user' : user})
    else:
        messages.error(request , "You are not logged in")
        return redirect('/login/')
    
def reject_service(request , req_id):
    user = request.user
    if user.is_authenticated:
        service_request = ServiceRequest.objects.get(req_id = req_id)
        service_request.request_status = 'rejected'
        service_request.save()
        messages.success(request , "Service request rejected successfully")
        return redirect('/profile/' , context = { 'user' : user})
    else:
        messages.error(request , "You are not logged in")
        return redirect('/login/')
    

def my_services(request):
    user  = request.user
    if user.is_authenticated and user.role == 'service_provider':
        service_provider = ServiceProvider.objects.get(user = user)   
        service_requests = ServiceRequest.objects.filter( service_provider = service_provider)
        return render(request , 'service/myservices.html' , {'service_requests':service_requests , 'isLoggedin':request.user.is_authenticated , 'user':request.user})
    messages.error(request , "You are not logged in")
    return redirect('/login/')