from django.urls import path

from tenant.views import TenantListCreateView

urlpatterns = [
    path('', TenantListCreateView.as_view()),
]