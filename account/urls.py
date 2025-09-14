from account.views import UserListCreate, UserDetailView, MyUserDetailView
from django.urls import path

urlpatterns = [
    path('',UserListCreate.as_view()),
    path('my-detail',MyUserDetailView.as_view()),
    path('<int:pk>',UserDetailView.as_view()),
]

