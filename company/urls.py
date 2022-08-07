from django.urls import path
from company import api


urlpatterns = [
    path('', api.CompanyListAPI.as_view()),
    path('<int:pk>', api.CompanyAPI.as_view()),
]
