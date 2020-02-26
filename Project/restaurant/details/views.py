from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import auth_logout
from django.shortcuts import redirect, render
from django.template.context_processors import request

# Create your views here.
def details(request):
    return render (request, 'details/index.html')

def auth_logout(request):
    logout(request)
    return redirect('login')