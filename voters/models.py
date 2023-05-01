from django.db import models
from django.utils import timezone


class NewsLetterSubscriber(models.Model):
    email = models.EmailField()
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-date_added",)

    def __str__(self):
        return f"{self.email}"
