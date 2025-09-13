from rest_framework.generics import ListCreateAPIView

from .models import PropertyMeter
from .serializers import PropertyMeterSerializer

class PropertyMeterListCreate(ListCreateAPIView):
    queryset = PropertyMeter.objects.all()
    serializer_class = PropertyMeterSerializer
