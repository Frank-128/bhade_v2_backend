from rest_framework import serializers

from tenant.models import Tenant


class TenantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tenant
        fields = ['id','first_name','last_name','email','phone_number','date_of_birth','created_at','updated_at']