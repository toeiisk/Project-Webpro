from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.template.context_processors import request


# Create your views here.
@login_required
def dashboard(request):
    return render (request, 'dashboard/index.html')

def edit(request):
    return render (request, 'dashboard/edit.html')

def add(request):
    return render (request, 'dashboard/add.html')
