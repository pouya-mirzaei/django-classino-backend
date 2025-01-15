import uuid
from django.db import models

# Create your models here.


class Discount(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    discount_percentage = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(null=True, default=True)
    code = models.TextField()

    class Meta:
        db_table = "discounts"

    def __str__(self):
        return f"{self.code} ({self.discount_percentage}%)"
