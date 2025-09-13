from django.urls import path

from contract.views import ContractListCreate

urlpatterns = [
    path('',ContractListCreate.as_view()),
]