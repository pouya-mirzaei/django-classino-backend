import uuid
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart_items")
    course = models.ForeignKey(
        "courses.Course", on_delete=models.CASCADE, related_name="cart_items"
    )
    added_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(null=True, default=False)

    class Meta:
        unique_together = ("user", "course")  # Prevent duplicate cart items
        ordering = ["-added_at"]  # Recently added items first
        db_table = "cart"

    def __str__(self):
        return f"{self.user.username} added {self.course.title} to cart"
