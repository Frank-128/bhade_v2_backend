from account.views import CreateUserView
from django.urls import path

urlpatterns = [
    path('create-user',CreateUserView.as_view()),
]

