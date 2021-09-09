from django.db import models
from django.db.models.deletion import CASCADE

class Provider(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    country_code = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=10, unique=True)
    language = models.CharField(max_length=16)
    currency = models.CharField(max_length=16)

    def __str__(self):
        return f'{self.name}'

class Service_area(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    polygon_name = models.CharField(max_length=50, unique=True)
    price = models.PositiveBigIntegerField()
    longitude = models.FloatField()
    latitude = models.FloatField()