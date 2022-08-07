from django.db import models
from device.models import Device


class Measurement(models.Model):
    device = models.ForeignKey(
        Device,
        to_field='device_id',
        on_delete=models.CASCADE
    )
    data = models.JSONField()
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.device_id)
