from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import auth_logout
from django.contrib.messages.api import success
from django.shortcuts import redirect, render
from django.template.context_processors import request

# Create your views here.
def dashboard(request):
    return render (request, 'dashboard/index.html')

def auth_logout(request):
    logout(request)
    return redirect('login')
