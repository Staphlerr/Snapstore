from django.db import models
import uuid

class MoodEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    description = models.TextField()
    price = models.IntegerField()

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5