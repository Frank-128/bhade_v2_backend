from django.urls import path

from meter.views import MeterListCreateView

urlpatterns = [
    path('', MeterListCreateView.as_view()),
]