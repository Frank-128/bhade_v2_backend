from rest_framework import serializers

from property_meter.models import PropertyMeter


class PropertyMeterSerializer(serializers.ModelSerializer):

    class Meta:
        model = PropertyMeter
        fields = '__all__'

