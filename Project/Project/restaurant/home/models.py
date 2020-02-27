
from django.db import models


# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=20)
    
class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    owner = models.CharField(max_length=20)
    picture = models.ImageField(upload_to="", height_field=None, width_field=None, max_length=None)
    open_time = models.TimeField()
    close_time = models.TimeField()
    rating = models.IntegerField()
    approve_by = models.CharField(max_length=20)
    approve_date = models.DateField()
    faculty_id = models.ForeignKey(Faculty, default=None, on_delete=models.CASCADE)