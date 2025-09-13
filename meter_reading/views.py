from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import MeterReadingSerializer
from meter_reading.models import MeterReading


class MeterReadingListCreateView(ListCreateAPIView):
    queryset = MeterReading.objects.all()
    serializer_class = MeterReadingSerializer