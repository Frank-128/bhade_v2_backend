from django.db import models
from block.models import Block

class Property(models.Model):
    property_no = models.IntegerField()
    name = models.CharField(max_length=100,unique=True)
    block = models.ForeignKey(Block, on_delete=models.CASCADE,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_name(self):
        return f'{self.name}  {self.property_no}'

    class Meta:
        db_table = 'property'
        unique_together = (('property_no', 'name','block'),)