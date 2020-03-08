from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import auth_logout
from django.contrib.messages.api import success
from django.db.models import Q
from django.shortcuts import redirect, render
from django.template.context_processors import request

from .models import Faculty, Restaurant


def index(request):
    faculty = Faculty.objects.all()
    restaurant = Restaurant.objects.all()
    
    return render (request, 'restaurant_home/index.html', context={'faculty': faculty, 'restaurant' : restaurant})

# def searchName(request):
#     qs = Restaurant.object.all()
#     inputName_query = request.GET.get('inputName')
#     print(inputName_query)
#     context = {
#         'queryset' : qs
#     }
#     return render(request, 'restaurant_home/login.html', context)

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
            return render(request, 'restaurant_home/login.html', context)
        pass
    else:
        return render(request, 'restaurant_home/login.html', context)

def auth_logout(request):
    logout(request)
    return redirect('login')
