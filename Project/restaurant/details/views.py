from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render
from django.template.context_processors import request

from restaurant_home.models import Food, Restaurant, RestaurantFood


# Create your views here.
def details(request, rest_id):
    restaurant = Restaurant.objects.filter(id=rest_id)
    restaurantfood = RestaurantFood.objects.filter(restaurant_id=rest_id)
    return render (request, 'details/index.html', context={'restaurant':restaurant, 'restaurantfood' : restaurantfood})

@login_required
@permission_required('restaurant.change_restaurantfood')
def restaurant_list(request):
    return HttpResponse('List Restaurant Page.')

@login_required
@permission_required('restaurant.restaurant_delete')
def restaurant_delete(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    restaurant.delete()
    return redirect('index')

@login_required
# @permission_required('restaurant.change_restaurantfood')
def food_list(request):
    return redirect('index')
