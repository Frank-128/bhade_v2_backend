from django.db import models

from contract.models import Contract
from property.models import Property
from tenant.models import Tenant

class PaymentChoices(models.TextChoices):
    RENT = 'rent'
    WATER = 'water'
    ELECTRICITY = 'electricity'

class Payment(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    type = models.CharField(choices=PaymentChoices.choices, max_length=15)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE,blank=True, null=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE,blank=True, null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    receipt = models.FileField(upload_to='payments/receipt', null=True, blank=True)
    paid_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tenant.first_name + " " + self.tenant.last_name

    class Meta:
        db_table = 'payment'
        ordering = ['-created_at']
