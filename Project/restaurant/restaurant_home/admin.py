from django.contrib import admin
from django.contrib.auth.models import Permission

from .models import *

class PriceInline(admin.TabularInline):
    model = RestaurantFood
    extra = 0
    
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['id' ,'name', 'approve_date', 'approve_by']
    list_per_page = 15

    list_filter = ['approve_date']
    search_fields = ['name']

class RestaurantFoodAdmin(admin.ModelAdmin):
    list_display = ['id' ,'food_id' ,'restaurant_id', 'price']
    list_per_page = 15

    list_filter = ['restaurant_id']

class FoodAdmin(admin.ModelAdmin):
    list_display = ['id' ,'name' ,'is_vegan']
    list_per_page = 15

    list_filter = ['is_vegan']
    search_fields = ['name']

    inlines = [PriceInline]

class RestaurantRatingAdmin(admin.ModelAdmin):
    list_display = ['id' ,'restaurant_id' ,'rating']
    list_per_page = 15

    list_filter = ['rating']


# Register your models here.
admin.site.register(Permission)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(RestaurantFood, RestaurantFoodAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(RestaurantRating, RestaurantRatingAdmin)

#Changing title admin page
admin.site.site_header = "KMITL - RESTAURANTS"
