from django.db import models
from django.utils import timezone
import secrets
from contestants.models import RegisterContestant

class VotePurchase(models.Model):
    ref = models.CharField(max_length=200)
    email = models.EmailField()
    number_of_votes = models.IntegerField(default=0)
    contestant_id = models.ForeignKey(RegisterContestant, on_delete=models.SET_NULL,null=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now, blank=True)
    
    class Meta:
        ordering = ("-amount",)

    def __str__(self):
        return f"Email:{self.email}|id:{self.id}"
    
    @property
    def total_price(self):
        total = self.amount * self.number_of_votes
        return str(total)

    def save(self,*args, **kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = VotePurchase.objects.filter(ref = ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)


class NewsLetterSubscriber(models.Model):
    email = models.EmailField()
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-date_added",)

    def __str__(self):
        return f"{self.email}"