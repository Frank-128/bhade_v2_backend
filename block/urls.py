from django.urls import path

from block.views import BlockList

urlpatterns = [
    path('',BlockList.as_view()),
]