from django.db import models
from property.models import Property

class PropertyPrice(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    amount = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'property_price'
        ordering = ['-created_at']