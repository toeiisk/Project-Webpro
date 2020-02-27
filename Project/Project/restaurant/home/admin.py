from webbrowser import register

from django.contrib import admin
from .models import Restaurant, Faculty
from django.contrib.auth.models import Permission

# Register your models here.
admin.site.register(Permission)
admin.site.register(Restaurant)
admin.site.register(Faculty)