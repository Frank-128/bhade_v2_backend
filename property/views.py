from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from property.models import Property
from property.serializers import PropertySerializer


class PropertListView(ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer