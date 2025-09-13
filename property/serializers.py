from rest_framework import serializers

from property.models import Property
from property.services import create_property


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

    def create(self, validated_data):
        return create_property(validated_data)