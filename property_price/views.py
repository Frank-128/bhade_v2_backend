from rest_framework.generics import ListCreateAPIView

from .models import  PropertyPrice
from .serializers import PropertyPriceSerializer

class PropertyPriceListCreateView(ListCreateAPIView):
    queryset = PropertyPrice.objects.all()
    serializer_class = PropertyPriceSerializer