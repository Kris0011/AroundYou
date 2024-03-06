from django.shortcuts import render
from authapp.models import ServiceProvider , CustomUser , Customer

# Create your views here.

def index(request):
    service_providers = ServiceProvider.objects.all()
    return render(request , 'services.html' , {'service_providers':service_providers , 'isLoggedin':request.user.is_authenticated , 'user':request.user})
