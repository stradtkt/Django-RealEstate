from django.shortcuts import render, redirect
from .models import *

def login(request):
    return render(request, 'accounts/login.html')

def register(request):
    return render(request, 'accounts/register.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    context = {}
    return render(request, 'accounts/dashboard.html', context)
