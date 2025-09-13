from django.db import models
from meter.models import Meter

class MeterReading(models.Model):
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE)
    reading = models.FloatField()
    reading_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'meter_reading'
        ordering = ['-created_at']