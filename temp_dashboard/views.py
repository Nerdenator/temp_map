from django.shortcuts import render

from .models import Sensor, Temperature


def dashboard(request):
    sensors = Sensor.objects.values()
    list_sensors = [sensor for sensor in sensors]
    temps_dictionary = {}
    for sensor in sensors:
        temps = Temperature.objects.filter(sensor_id=sensor['id'])
        temps_dictionary.update({sensor['location']: temps})

    return render(request, 'temp_dashboard/index.html', {'sensors': list_sensors, 'temps_dictionary': temps_dictionary})

