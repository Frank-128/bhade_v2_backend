from django.urls import path
from meter_reading.views import MeterReadingListCreateView

urlpatterns = [
    path('', MeterReadingListCreateView.as_view()),
]