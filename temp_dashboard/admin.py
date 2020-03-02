from django.contrib import admin

# Register your models here.
from .models import Temperature, Sensor

admin.site.register(Temperature)
admin.site.register(Sensor)