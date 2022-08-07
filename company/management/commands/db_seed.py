from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
import random
from company.models import Company
from device.models import Device
from measurement.models import Measurement

fake = Faker()

labels = ['home', 'city', 'building', 'construction', 'label']
sampled_list = random.sample(labels, 3)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for _ in range(10):
            Company.objects.create(
                name=fake.name(),
                location=fake.address()
            )
        for _ in range(100):
            device = Device.objects.create(
                company=Company(random.randint(1, 10)),
                labels=random.sample(labels, 3)
            )
            for _ in range(10):
                Measurement.objects.create(
                    device=device,
                    data={
                        "temperature": [random.randint(1, 20), random.randint(21, 50)],
                        "rssi": [random.randint(0, 20), random.randint(21, 50)],
                        "humidity": [random.randint(0, 50), random.randint(51, 100)],
                    },
                    date=fake.date_time(tzinfo=timezone.utc),
                )

        self.stdout.write("DB Seed is done")
