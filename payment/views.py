from rest_framework.generics import ListCreateAPIView
from .models import Payment
from .serializers import PaymentSerializer

class PaymentListCreateView(ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
