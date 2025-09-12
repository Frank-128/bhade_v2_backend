from django.db import models
from block.models import Block

class Property(models.Model):
    property_no = models.IntegerField()
    name = models.CharField(max_length=100)
    block = models.ForeignKey(Block, on_delete=models.CASCADE,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'property'