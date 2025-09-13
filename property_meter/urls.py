from django.urls import path

from property_meter.views import PropertyMeterListCreate

urlpatterns = [
    path('', PropertyMeterListCreate.as_view()),
]