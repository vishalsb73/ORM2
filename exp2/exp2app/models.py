from django.db import models
from django.contrib import admin
class Car(models.Model):
    Car_name = models.CharField()
    Car_model= models.CharField()
    release_date = models.DateField()
    Mileage= models.CharField()
class CarAdmin(admin.ModelAdmin):
    list_display = ('Car_name', 'Car_model', 'release_date', 'Mileage')

