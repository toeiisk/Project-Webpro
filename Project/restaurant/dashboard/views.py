from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from django.template.context_processors import request

from details.views import *
from restaurant_home.views import *


# Create your views here.
@login_required
def dashboard(request):
    if request.user.is_superuser:
        faculty = Faculty.objects.all()
        restaurant = Restaurant.objects.all()
        return render (request, 'dashboard/index.html', context={'faculty': faculty, 'restaurant' : restaurant})
    else:
        return redirect('login')

@login_required
def restaurant_add(request):
    if request.user.is_superuser:
        return HttpResponse('Add Restaurant Page.')
    else:
        return redirect('login')
