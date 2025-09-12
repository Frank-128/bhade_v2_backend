from django.db import models
from meter.models import Meter
from property.models import Property

class PropertyMeter(models.Model):
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.property.name + " " + self.meter.meter_no

    class Meta:
        db_table = 'property_meter'
