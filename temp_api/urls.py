from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from temp_api import views

urlpatterns = [
    path('temperatures/', views.temperature_list),
    path('temperatures/<int:sensor_id>', views.temperature_latest),
    path('sensors/', views.sensor_list)
]

urlpatterns = format_suffix_patterns(urlpatterns)