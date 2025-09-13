from rest_framework.generics import ListAPIView, ListCreateAPIView

from .serializers import BlockSerializer
from .models import Block

class BlockList(ListCreateAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer