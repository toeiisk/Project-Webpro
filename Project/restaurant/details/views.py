from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render
from django.template.context_processors import request

from restaurant_home.models import Food, Restaurant, RestaurantFood


# Create your views here.
def details(request, rest_id):
    restaurant = Restaurant.objects.filter(id=rest_id)
    food = Food.objects.all()
    restaurantfood = RestaurantFood.objects.all()
    return render (request, 'details/index.html', context={'restaurant':restaurant, 'food' : food, 'restaurantfood' : restaurantfood})

def restaurant_list(request):
    return HttpResponse('List Restaurant Page.')

@login_required
@permission_required('details.restaurant_delete')
def restaurant_delete(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    restaurant.delete()
    return redirect('index')
