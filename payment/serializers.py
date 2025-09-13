from rest_framework import serializers

from payment.models import Payment
from payment.services import create_payment


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['tenant'] = instance.tenant.full_name
        return data

    def create(self, validated_data):
        return create_payment(validated_data)
