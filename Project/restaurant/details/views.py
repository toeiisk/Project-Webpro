from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render
from django.template.context_processors import request
from restaurant_home.models import *


# Create your views here.
def details(request, rest_id):
    restaurant = Restaurant.objects.filter(id=rest_id)
    restaurantfood = RestaurantFood.objects.filter(restaurant_id=rest_id)
    return render (request, 'details/index.html', context={'restaurant':restaurant, 'restaurantfood' : restaurantfood})

#function Change รายละเอียดของ Restaurant
@login_required
@permission_required('details.change_restaurant')
def restaurant_list(request):
    if request.user.is_superuser:
        return HttpResponse('List Restaurant Page.')
    else:
        return redirect('index')

#function Delete รายละเอียดของ Restaurant 
@login_required
@permission_required('details.delete_restaurant')
def restaurant_delete(request, restaurant_id):
    if request.user.is_superuser:
        restaurant = Restaurant.objects.get(id=restaurant_id)
        restaurant.delete()
        return redirect('index')
    else:
        return redirect('index')

#function Add รายละเอียดของ Food
@login_required
@permission_required('details.add_food')
def food_add(request):
    if request.user.is_superuser:
        return HttpResponse('Add Food Page.')
    else:
        return redirect('index')

#function Change รายละเอียดของ Food
@login_required
@permission_required('details.change_food')
def food_list(request):
    if request.user.is_superuser:
        return HttpResponse('List Food Page.')
    else:
        return redirect('index')

#function Delete รายละเอียดของ Food
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
        rest_id = request.POST.get('rest_id') # ดึง rest id ที่มีการส่งเข้ามา
        score = request.POST.get('score') # ดึง score ค่าที่ถูกส่งเข้ามา
        new_rating = RestaurantRating(restaurant_id_id=rest_id, rating=score) #เก็บค่า rate กับ rest id ที่ส่งเข้ามาในตัวแปร new_rating
        new_rating.save() #บันทึก
        all_rating = RestaurantRating.objects.filter(restaurant_id_id=rest_id) #เช็คเอาค่า rate ที่มี restaurant_id กับ rest_id ตรงกัน
        rates = 0   #กำหนดค่าตัวแปร
        for rt in all_rating: #วน loop เอาค่า rating ทั้งหมดใน all_rating
            rates += rt.rating #เอาค่า rating ทั้งหมดบวกรวมกันบวกเข้ากับ rates
        rates /= all_rating.count() #นับจำนวนค่าที่มีทั้งหมดใน all_rating เพื่อนำมาเป็นตัวหารหาค่าเฉลี่ย
        print(rates)
        current_restaurant = Restaurant.objects.get(id=rest_id)
        current_restaurant.rating = rates #update ค่า rating ให้เท่ากับ rates ที่ผ่านการคำนวณมา
        current_restaurant.save() #บันทึก
    return redirect('index')