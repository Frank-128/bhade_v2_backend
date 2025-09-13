from .models import Property

def create_property(data):
    return Property.objects.create(**data)
