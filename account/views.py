from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from account.serializers import UserSerializer


class CreateUserView(APIView):

    def post(self,request,*args,**kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('User created successfully',status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)