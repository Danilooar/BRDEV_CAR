from django.db import models # type: ignore

class Brand(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=200)

      
  def __str__(self):
    return self.name
  
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='car_brand')
    factory_year = models.IntegerField()
    model_year = models.IntegerField()
    plate = models.CharField(max_length=10, unique=True,null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='cars/',blank=True, null=True)
   
   
    def __str__(self):
     return self.model
