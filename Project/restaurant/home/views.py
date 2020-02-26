from astroid import objects
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import auth_logout
from django.contrib.messages.api import success
from django.shortcuts import redirect, render
from django.template.context_processors import request

from home.models import Faculty


def index(request):
    faculty = Faculty.objects.all()
    return render(request, 'home/index.html', context={'faculty': faculty})

def auth_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            error = "Username or Password Incorrect!!"
            context['username'] = username
            context['password'] = password
            context['error'] = "Username or Password Incorrect!!"
            return render(request, 'home/login.html', context)
        pass
    else:
        return render(request, 'home/login.html', context)

def auth_logout(request):
    logout(request)
    return redirect('login')
