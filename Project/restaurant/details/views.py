from django.shortcuts import redirect, render
from django.template.context_processors import request
from restaurant_home.models import Restaurant

# Create your views here.
def details(request, rest_id):
    restaurant = Restaurant.objects.filter(id=rest_id)
    return render (request, 'details/index.html', context={'restaurant':restaurant})