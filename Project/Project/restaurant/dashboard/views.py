from django.shortcuts import redirect, render
from django.template.context_processors import request
from home.models import Faculty

# Create your views here.
def dashboard(request):
    faculty = Faculty.objects.all()
    return render (request, 'dashboard/index.html', context={'faculty': faculty})

def edit(request):
    return render (request, 'dashboard/edit.html')

def add(request):
    return render (request, 'dashboard/add.html')
