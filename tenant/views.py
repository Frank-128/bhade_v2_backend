from rest_framework.generics import ListCreateAPIView
from .serializers import TenantSerializer
from tenant.models import Tenant


class TenantListCreateView(ListCreateAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

