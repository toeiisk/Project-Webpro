from django.urls import path
from . import views
from details.views import *

urlpatterns = [
    path('<int:rest_id>', details, name='details'),
    path('restaurant/delete/<int:restaurant_id>/', views.restaurant_delete, name='restaurant_delete'),
    path('admin/restaurant_home/restaurant/<int:restaurant_id>/change/', views.restaurant_list, name='restaurant_list'),
    path('admin/restaurant_home/food/add/', food_add, name='food_add'),
    path('admin/restaurant_home/restaurantfood/add/', food_price, name='food_price'),
    path('admin/restaurant_home/food/<int:food_id>/change/', views.food_list, name='food_list'),
    path('admin/restaurant_home/restaurantfood/<int:food_id>/change/', views.food_list_price, name='food_list_price'),
    path('food/delete/<int:food_id>/', views.food_delete, name='food_delete'),
    path('rating_score/', views.rating_score, name='rating_score'),
]