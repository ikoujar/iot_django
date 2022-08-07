from django_filters import rest_framework as filters
from .models import Device


class LabelsFilter(filters.BaseCSVFilter, filters.CharFilter):
    pass


class DeviceFilter(filters.FilterSet):
    labels = LabelsFilter(field_name='labels', lookup_expr='contains')

    class Meta:
        model = Device
        fields = ['company', 'labels']

