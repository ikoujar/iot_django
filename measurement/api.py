from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from . import filters
from . import serializers


class MeasurementListAPI(generics.ListCreateAPIView):

    serializer_class = serializers.MeasurementSerializer
    model = serializer_class.Meta.model
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.MeasurementFilter

    def get_queryset(self):
        return self.model.objects.select_related('device__company').all()


class MeasurementTemperatureListAPI(generics.ListAPIView):

    serializer_class = serializers.MeasurementTemperatureSerializer
    model = serializer_class.Meta.model
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.MeasurementFilter

    def get_queryset(self):
        return self.model.objects.select_related('device').filter(data__has_key='temperature')
