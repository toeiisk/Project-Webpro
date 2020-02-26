from django.shortcuts import render
from django.template.context_processors import request


# Create your views here.
def dashboard(request):
    return render (request, 'dashboard/index.html')
