from django.shortcuts import redirect, render
from django.template.context_processors import request

# Create your views here.
def details(request):
    return render (request, 'details/index.html')