from django.db import models
from django.contrib.auth.models import User
import uuid

class ItemEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    description = models.TextField()
    price = models.IntegerField()

    @property
    def is_price_expensive(self):
        return self.price > 1000