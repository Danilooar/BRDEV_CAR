from django.db import models  # type: ignore
from model_utils import FieldTracker  

class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="car_brand")
    factory_year = models.IntegerField()
    model_year = models.IntegerField()
    km = models.IntegerField(blank=True, null=True,default=0)
    plate = models.CharField(max_length=10, unique=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to="cars/", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    tracker = FieldTracker(fields=['brand', 'model', 'model_year'])
    
    def __str__(self):
        return self.model
