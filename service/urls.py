from django.urls import path 
from . import views

urlpatterns = [
    path('allservices/' , views.index , name='index') ,
    path('myservices/' , views.my_services , name='my_services'),
    path('request/<int:sp_id>/' , views.request_service , name='request_service') ,
    path('complete_service/<int:req_id>/', views.complete_service, name='complete_service'),
    path('accept_service/<int:req_id>/', views.accept_service, name='accept_service'),
    path('reject_service/<int:req_id>/', views.reject_service, name='reject_service'),
]