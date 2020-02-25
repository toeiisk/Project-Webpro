from django.contrib.auth import authenticate
from django.contrib.messages.api import success
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.context_processors import request


def index(request):
    return render(request, 'home/index.html')

def login(request):
    context = {}
    if request.method == "post":
        username = request.post['username']
        username = request.post['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reversed('user_success'))
        else:
            context["error"] = "Username or Password Incorrect!!"
            return render(request, 'home/login.html', context)
        pass
    else:
        return render(request, 'home/login.html', context)

def success(request):
    context = {}
    context['user'] = request.user
    return render(request, 'home/success.html', context)

def user_logout(request):
    if request.method == "post":
        logout(request)
        return HttpResponseRedirect(reversed('user_login'))