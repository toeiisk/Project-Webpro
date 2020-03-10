from django.db import models

# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="", height_field=None, width_field=None, max_length=None)
    open_time = models.TimeField()
    close_time = models.TimeField()
    rating = models.FloatField(default=0.0)
    approve_by = models.CharField(max_length=50)
    approve_date = models.DateField()
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=50)
    is_vegan = models.BooleanField()

    def __str__(self):
        return self.name

class RestaurantFood(models.Model):
    price = models.FloatField()
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)
    food_id = models.ForeignKey(Food, on_delete=models.DO_NOTHING)

class RestaurantRating(models.Model):
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rate = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    rating = models.IntegerField(choices=rate, default=1)

