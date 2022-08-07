from rest_framework import generics
from device.serializers import DeviceSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import DeviceFilter


class DeviceAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DeviceSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        return self.model.objects.all()


class DeviceListAPI(generics.ListCreateAPIView):
    serializer_class = DeviceSerializer
    model = serializer_class.Meta.model
    filter_backends = [DjangoFilterBackend]
    filterset_class = DeviceFilter

    def get_queryset(self):
        return self.model.objects.all()
