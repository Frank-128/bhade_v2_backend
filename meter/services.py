from .models import Meter

def create_meter(data):
    return Meter.objects.create(**data)