from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Useraccount
        # fields='__all__'
        fields=['name','email','password','username','user_interest']  

class SendotpSerializer(serializers.ModelSerializer):
    class Meta:
        model=Useraccount
        fields=['email','is_verified']

class VerifyOtpSerializer(serializers.Serializer):
    email=serializers.EmailField()      
    otp=serializers.CharField()    

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=Useraccount
        fields=['password','email']

        fields=['id','interest']        
             
