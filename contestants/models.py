import secrets
from PIL import Image
from django.db import models
from django.utils import timezone

class RegistrationPurchase(models.Model):
    ref = models.CharField(max_length=200)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=15, default="08000000000", null=True)
    verified = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"Email:{self.email}|id:{self.id}"

    def save(self,*args, **kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = RegistrationPurchase.objects.filter(ref = ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)

class RegisterContestant(models.Model):
    refnum = models.CharField(max_length=200)
    firstname = models.CharField(max_length=30,blank=False)
    lastname = models.CharField(max_length=30,blank=False)
    instagram_handle = models.CharField(max_length=30,blank=False)
    tell_us = models.TextField(default="I WANT TO WIN")
    email = models.EmailField()
    phonenumber = models.CharField(max_length=20)
    image1 = models.ImageField(default="defaultuser.jpg", upload_to="contestant/%Y/%m/%d")
    image2 = models.ImageField(default="defaultuser.jpg", upload_to="contestant/%Y/%m/%d")
    gender = models.CharField(max_length=10)
    number_of_votes = models.IntegerField(default=0)
    is_evicted = models.BooleanField(default=False)
    is_confirmed = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        ordering = ("-number_of_votes",)

    def __str__(self):
        return f"{self.firstname}|{self.id}"

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image1.path)
        if img.height > 120 or img.width > 120:
            img = img.resize((800,800), Image.ANTIALIAS)
            img.save(self.image1.path)

        img2 = Image.open(self.image2.path)
        if img2.height > 120 or img2.width > 120:
            img2 = img2.resize((800,800), Image.ANTIALIAS)
            img2.save(self.image2.path)
            
    @property
    def fullname(self):
        return f"{self.lastname} {self.firstname}"