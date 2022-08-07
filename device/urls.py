from django.urls import path
from . import api

urlpatterns = [
    path('', api.DeviceListAPI.as_view()),
    path('<int:pk>', api.DeviceAPI.as_view()),
]
