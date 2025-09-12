from django.db import models
from property.models import Property

class PropertyPrice(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)