from django.db import models

from tenant.models import Tenant
from property.models import Property

class Contract(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    attachment = models.FileField(upload_to='tenants/attachments/',blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.property.name + " " + self.tenant.first_name + " " + self.tenant.last_name

    class Meta:
        db_table = 'contract'

