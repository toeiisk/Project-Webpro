from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import *

# Register your models here.
admin.site.register(Permission)
admin.site.register(Restaurant)
admin.site.register(Faculty)
admin.site.register(RestaurantFood)
admin.site.register(Food)

#Changing title admin page
admin.site.site_header = "KMITL - RESTAURANTS"

class Faculty(admin.ModelAdmin):
    list_display = ('name')

class Restaurant(admin.ModelAdmin):
    list_display = ('name')
