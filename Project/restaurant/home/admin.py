from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import Restaurant, Faculty

# Register your models here.
admin.site.register(Permission)
admin.site.register(Restaurant)
admin.site.register(Faculty)