from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.template.context_processors import request
from restaurant_home.views import *
from details.views import *

# Create your views here.
@login_required
def dashboard(request):
    faculty = Faculty.objects.all()
    restaurant = Restaurant.objects.all()
    return render (request, 'dashboard/index.html', context={'faculty': faculty, 'restaurant' : restaurant})

@login_required
def restaurant_add(request):
    return HttpResponse('Add Restaurant Page.')
