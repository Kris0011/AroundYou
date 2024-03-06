from django.urls import path 
from . import views

urlpatterns = [
    path('' , views.index , name='index') ,
    path('request/<int:sp_id>/' , views.request_service , name='request_service') 
]