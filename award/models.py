import secrets
from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField


class AwardsCategory(models.Model):
    name = models.CharField(max_length=150)
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Awards categories"

    def __str__(self):
        return f"{self.name}"


class AwardsContestant(models.Model):
    category = models.ForeignKey(
        AwardsCategory, on_delete=models.SET_DEFAULT, default='unknown')
    firstname = models.CharField(max_length=30, blank=False)
    lastname = models.CharField(max_length=30, blank=True, null=True)
    instagram_handle = models.CharField(max_length=30, blank=True, null=True)
    tell_us = models.TextField(default="I WANT TO WIN")
    email = models.EmailField(blank=True, null=True)
    phonenumber = models.CharField(max_length=20, blank=True, null=True)
    image1 = CloudinaryField("image")
    gender = models.CharField(max_length=10)
    number_of_votes = models.IntegerField(default=0)
    is_evicted = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"{self.firstname}|{self.id}"

    @property
    def fullname(self):
        if self.lastname == None:
            return f"{self.firstname}"
        if self.firstname == None:
            return f"{self.lastname}"
        else:
            return f"{self.lastname} {self.firstname}"


class AwardVotePurchase(models.Model):
    ref = models.CharField(max_length=200)
    email = models.EmailField()
    number_of_votes = models.IntegerField(default=0)
    contestant_id = models.ForeignKey(
        AwardsContestant, on_delete=models.SET_NULL, null=True)
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

    def save(self, *args, **kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = AwardVotePurchase.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)
