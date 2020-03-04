from django.db import models

# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=50)
    
class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="", height_field=None, width_field=None, max_length=None)
    open_time = models.TimeField()
    close_time = models.TimeField()
    rating = models.IntegerField()
    approve_by = models.CharField(max_length=50)
    approve_date = models.DateField()
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)

class Food(models.Model):
    name = models.CharField(max_length=50)
    is_vegan = models.BooleanField()

class RestaurantFood(models.Model):
    price = models.FloatField()
    restaurant_id = models.ManyToManyField(Restaurant)
    food_id = models.ManyToManyField(Food) 
