from django.urls import path
from . import views
from dashboard.views import dashboard, restaurant_add

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('admin/restaurant_home/restaurant/add/', restaurant_add, name='restaurant_add'),
    path('restaurant/delete/<int:restaurant_id>/', views.restaurant_delete, name='restaurant_delete'),
    path('admin/restaurant_home/restaurant/<int:restaurant_id>/change/', views.restaurant_list, name='restaurant_list'),
]