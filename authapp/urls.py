from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name='home'),
    path('register/' , views.register_request , name='register'),
    path('login/' , views.login_request , name='login'),
    path('logout/' , views.logout_request , name='logout'),
    path('set_customer_details/' , views.set_customer_details , name='set_customer_details'),
    path('set_profile/' , views.set_profile , name='set_profile'),
]

