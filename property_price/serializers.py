from rest_framework import serializers

from property_price.models import PropertyPrice


class PropertyPriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = PropertyPrice
        fields = ['id','property','amount','start_date','end_date','created_at','updated_at']



