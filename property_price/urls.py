from django.urls import path

from property_price.views import PropertyPriceListCreateView

urlpatterns = [
    path('',PropertyPriceListCreateView.as_view()),
]

