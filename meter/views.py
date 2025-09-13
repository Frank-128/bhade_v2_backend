from rest_framework.generics import ListCreateAPIView

from .models import Meter
from .serializers import MeterSerializer

class MeterListCreateView(ListCreateAPIView):
    queryset = Meter.objects.all()
    serializer_class = MeterSerializer
