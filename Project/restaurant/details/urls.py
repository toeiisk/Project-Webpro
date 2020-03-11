from django.urls import path
from . import views
from details.views import *

urlpatterns = [
    path('<int:rest_id>', details, name='details'),
    path('admin/restaurant_home/food/add/', food_add, name='food_add'),
    path('admin/restaurant_home/food/<int:food_id>/change/', views.food_list, name='food_list'),
    path('food/delete/<int:food_id>/', views.food_delete, name='food_delete'),
    path('rating_score/', views.rating_score, name='rating_score'),
]