from django.db import models


# Create your models here.
class Sensor(models.Model):
    location = models.CharField(max_length=20)
    ip_address = models.GenericIPAddressField()


class Temperature(models.Model):
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    fahrenheit = models.DecimalField(max_digits=5, decimal_places=2)
    celsius = models.DecimalField(max_digits=5, decimal_places=2)