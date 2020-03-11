from django.urls import path
from . import views
from dashboard.views import dashboard, restaurant_add

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('admin/restaurant_home/restaurant/add/', views.restaurant_add, name='restaurant_add'), #ใช้กับปุ่ม add restaurant ในหน้า dashboard
    path('restaurant/delete/<int:restaurant_id>/', views.restaurant_delete, name='restaurant_delete'), #import มาจากของ details ใช้กับปุ่ม delete restaurant
    path('admin/restaurant_home/restaurant/<int:restaurant_id>/change/', views.restaurant_list, name='restaurant_list'), #import มาจากของ details ใช้กับปุ่ม edit restaurant
]