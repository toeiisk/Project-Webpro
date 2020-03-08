from django.urls import path
from . import views
from dashboard.views import dashboard, edit, add

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('admin/restaurant_home/restaurant', edit, name='edit'),
    path('admin/restaurant_home/restaurant/add', edit, name='add'),
]