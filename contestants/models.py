import secrets
from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField


class RegistrationPurchase(models.Model):
    ref = models.CharField(max_length=200)
    email = models.EmailField()
    phonenumber = models.CharField(
        max_length=15, default="08000000000", null=True)
    verified = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"Email:{self.email}|id:{self.id}"

    def save(self, *args, **kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = RegistrationPurchase.objects.filter(
                ref=ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)


class RegisterContestant(models.Model):
    refnum = models.CharField(max_length=200)
    firstname = models.CharField(max_length=30, blank=False)
    lastname = models.CharField(max_length=30, blank=True, null=True)
    instagram_handle = models.CharField(max_length=30, blank=False, null=True)
    tell_us = models.TextField(default="I WANT TO WIN")
    email = models.EmailField(blank=True, null=True)
    phonenumber = models.CharField(max_length=20, blank=True, null=True)
    image1 = CloudinaryField("image")
    gender = models.CharField(max_length=10)
    number_of_votes = models.IntegerField(default=0)
    is_evicted = models.BooleanField(default=False)
    is_confirmed = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        ordering = ("-number_of_votes",)

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
