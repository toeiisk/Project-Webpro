from django.urls import path
from . import views
from details.views import *

urlpatterns = [
    path('<int:rest_id>', details, name='details'),
    path('admin/restaurant_home/food/add/', food_add, name='food_add'), #ใช้กับปุ่ม add food
    path('admin/restaurant_home/food/<int:food_id>/change/', views.food_list, name='food_list'), #ใช้กับปุ่ม edit food
    path('food/delete/<int:food_id>/', views.food_delete, name='food_delete'), #ใช้กับปุ่ม delete food
    path('rating_score/', views.rating_score, name='rating_score'),
]