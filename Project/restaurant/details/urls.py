from django.urls import path
from . import views
from details.views import *

urlpatterns = [
    path('<int:rest_id>', details, name='details'),
    path('restaurant/delete/<int:restaurant_id>/', views.restaurant_delete, name='restaurant_delete'),
    path('admin/restaurant_home/restaurant/<int:restaurant_id>/change/', views.restaurant_list, name='restaurant_list')
]