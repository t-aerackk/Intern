from django.shortcuts import render, redirect
from .models import *
from django.template import loader
# from django.http import HttpResponse for http requests only

# Create your views here.
def Patient_view(request):
    return render(request, 'patient_list.html',)

# def patient(request):
#     return HttpResponse("Hello world") 

def home(request):
    return render(request,'homepage.html') 
