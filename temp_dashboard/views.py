from django.shortcuts import render

from .models import Sensor, Temperature


def dashboard(request):
    sensors = Sensor.objects.values()
    list_sensors = [sensor for sensor in sensors]
    return render(request, 'temp_dashboard/index.html', {'sensors': list_sensors})