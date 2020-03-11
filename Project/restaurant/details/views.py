from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render
from django.template.context_processors import request
from restaurant_home.models import *


# Create your views here.
def details(request, rest_id):
    restaurant = Restaurant.objects.filter(id=rest_id)
    restaurantfood = RestaurantFood.objects.filter(restaurant_id=rest_id)
    return render (request, 'details/index.html', context={'restaurant':restaurant, 'restaurantfood' : restaurantfood})

@login_required
@permission_required('details.change_restaurant')
def restaurant_list(request):
    if request.user.is_superuser:
        return HttpResponse('List Restaurant Page.')
    else:
        return redirect('index')
        
@login_required
@permission_required('details.delete_restaurant')
def restaurant_delete(request, restaurant_id):
    if request.user.is_superuser:
        restaurant = Restaurant.objects.get(id=restaurant_id)
        restaurant.delete()
        return redirect('index')
    else:
        return redirect('index')

@login_required
@permission_required('details.add_food')
def food_add(request):
    if request.user.is_superuser:
        return HttpResponse('Add Food Page.')
    else:
        return redirect('index')

@login_required
@permission_required('details.change_food')
def food_list(request):
    if request.user.is_superuser:
        return HttpResponse('List Food Page.')
    else:
        return redirect('index')

@login_required
@permission_required('details.delete_food')
def food_delete(request, food_id):
    if request.user.is_superuser:
        food = Food.objects.get(id=food_id)
        food.delete()
        return redirect('index')
    else:
        return redirect('index')

def rating_score(request):
    context = {}
    if request.method == "POST":
        rest_id = request.POST.get('rest_id')
        score = request.POST.get('score')
        new_rating = RestaurantRating(restaurant_id_id=rest_id, rating=score)
        new_rating.save()
        all_rating = RestaurantRating.objects.filter(restaurant_id_id=rest_id)
        rates = 0
        for rt in all_rating:
            rates += rt.rating
        rates /= all_rating.count()
        print(rates)
        current_restaurant = Restaurant.objects.get(id=rest_id)
        current_restaurant.rating = rates
        current_restaurant.save()
    return redirect('index')