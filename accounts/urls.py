from django.contrib import admin
from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    # path('',registeration),
    # path('register',register),
    path('v1/register',RegisterAPI.as_view()),
    path('v2/sendotp',SendOtpAPI.as_view()),
    path('v3/verifyotp',VerifyOtpAPI.as_view()),
    path('v4/login',LoginAPI.as_view()),
    
]