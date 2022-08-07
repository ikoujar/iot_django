from django_filters import rest_framework as filters

from company.models import Company
from .models import Measurement


class MeasurementFilter(filters.FilterSet):

    company = filters.ModelChoiceFilter(field_name='device__company', queryset=Company.objects.filter())
    time = filters.DateTimeFromToRangeFilter(field_name='date')

    class Meta:
        model = Measurement
        fields = ['device', 'company', 'time']
