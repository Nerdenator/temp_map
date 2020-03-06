from django.shortcuts import render

from .models import Sensor, Temperature


def dashboard(request):
    sensors = Sensor.objects.all()
    return render(request, 'temp_dashboard/index.html', {'sensors': sensors})