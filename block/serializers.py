from rest_framework import serializers
from .models import Block
from .services import create_block


class BlockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Block
        fields = ['name','code']
        extra_kwargs = {'code': {'required': False}}

    def create(self, validated_data):
        return create_block(validated_data)