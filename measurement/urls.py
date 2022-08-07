from django.urls import path
from . import api


urlpatterns = [
    path('', api.MeasurementListAPI.as_view()),
    path('temperature', api.MeasurementTemperatureListAPI.as_view()),
]
