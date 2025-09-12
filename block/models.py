from django.db import models

class Block(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'block'
        ordering = ['created_at']