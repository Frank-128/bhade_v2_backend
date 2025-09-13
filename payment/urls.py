from django.urls import path
from payment.views import PaymentListCreateView

urlpatterns = [
    path('', PaymentListCreateView.as_view()),
]