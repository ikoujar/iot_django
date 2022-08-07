from rest_framework import serializers
from .models import Measurement
from datetime import datetime
import numpy as np


class TimestampField(serializers.IntegerField):

    def to_internal_value(self, data):
        return datetime.fromtimestamp(int(data))

    def to_representation(self, value):
        return int(value.timestamp())


class MeasurementSerializer(serializers.ModelSerializer):
    time = TimestampField(source='date')

    class Meta:
        model = Measurement
        fields = ('device', 'data', 'time')


class MeasurementTemperatureSerializer(serializers.ModelSerializer):
    time = TimestampField(source='date')
    avg_temperature = serializers.SerializerMethodField('get_avg_temperature')
    temperature = serializers.SerializerMethodField('get_temperature')

    @staticmethod
    def get_temperature(obj):
        return obj.data['temperature']

    @staticmethod
    def get_avg_temperature(obj):
        total = np.sum(obj.data['temperature'])
        return total / len(obj.data['temperature'])

    class Meta:
        model = Measurement
        fields = ('device', 'temperature', 'avg_temperature', 'time')
