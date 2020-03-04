from django.contrib import admin
from .models import Faculty, Restaurant, RestaurantFood, Food
from django.contrib.auth.models import Permission

# Register your models here.
admin.site.register(Permission)
admin.site.register(Restaurant)
admin.site.register(Faculty)
admin.site.register(RestaurantFood)
admin.site.register(Food)