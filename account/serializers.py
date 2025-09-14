from account.models import User
from rest_framework import serializers

from account.services import create_new_user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name','last_name','email','phone_number','role']


    def create(self,validated_data):
        return create_new_user(validated_data)
