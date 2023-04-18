from django.shortcuts import render,HttpResponse, redirect
from .api import  *
from django.views.decorators.csrf import requires_csrf_token

# ALL the content of this file is in api.py

# @requires_csrf_token
# def registeration(request):
#     if request.method == 'POST':
#         response=RegisterAPI(request)
#         return response
#     else:
#         return render(request,'index.html')

# def register(request):
#     return HttpResponse('Welcome')