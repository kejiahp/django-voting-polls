import secrets
from django.db import models
from django.utils import timezone
from award.models import AwardsContestant


class WebhookTestModel(models.Model):
    ref = models.CharField(max_length=200)

    def __str__(self):
        return f"Reference {self.ref}"


class AwardVotingWebhookModel(models.Model):
    payment_state_choice = (
        ('success', 'success'),
        ('failed', 'failed'),
        ('pending', 'pending'),
    )

    ref = models.CharField(max_length=200)
    email = models.EmailField()
    number_of_votes = models.IntegerField(default=0)
    contestant_id = models.ForeignKey(
        AwardsContestant, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    verified = models.BooleanField(default=False)
    order_paid = models.BooleanField(default=False)
    payment_state = models.CharField(
        choices=payment_state_choice, max_length=15, default='pending')
    date_created = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        ordering = ("-amount",)

    def __str__(self):
        return f"Email:{self.email}|id:{self.id}"

    @property
    def total_price(self):
        total = self.amount * self.number_of_votes
        return str(total)

    def save(self, *args, **kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = AwardVotingWebhookModel.objects.filter(
                ref=ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)
