from django.urls import path

from .views import PropertListView

urlpatterns = [
    path('',PropertListView.as_view()),
]