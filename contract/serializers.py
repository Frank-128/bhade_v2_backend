from rest_framework import serializers

from contract.models import Contract


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['tenant','property','attachment','start_date','end_date','created_at','updated_at']


    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['tenant'] = instance.tenant.full_name
        data['property'] = instance.property.name
        return data