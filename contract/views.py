from rest_framework.generics import ListCreateAPIView
from .models import Contract
from .serializers import ContractSerializer

class ContractListCreate(ListCreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer