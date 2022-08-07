from django.db import models
from company.models import Company
from django.contrib.postgres.fields import ArrayField
import uuid


class Device(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )
    device_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )
    active = models.BooleanField(default=True)
    labels = ArrayField(
        models.CharField(max_length=512, null=True, blank=True),
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.device_id)
