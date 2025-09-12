from django.db import models

class Meter(models.Model):
    meter_no = models.CharField(max_length=20)
    status = models.BooleanField(default=False)
    installed_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meter_no

    class Meta:
        db_table = 'meter'
