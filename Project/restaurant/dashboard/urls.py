from django.urls import path
from . import views
from dashboard.views import dashboard, restaurant_add
from details.urls import *

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('admin/restaurant_home/restaurant/add/', restaurant_add, name='restaurant_add'),
]