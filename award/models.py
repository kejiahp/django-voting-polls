import secrets
from django.db import models
from django.utils import timezone
from PIL import Image

class AwardsCategory(models.Model):
    name = models.CharField(max_length=150)
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural ="Awards categories"

    def __str__(self):
        return f"{self.name}"


class AwardsContestant(models.Model):
    category = models.ForeignKey(AwardsCategory, on_delete=models.SET_DEFAULT,default='unknown')
    firstname = models.CharField(max_length=30,blank=False)
    lastname = models.CharField(max_length=30,blank=False)
    instagram_handle = models.CharField(max_length=30,blank=False)
    tell_us = models.TextField(default="I WANT TO WIN")
    email = models.EmailField()
    phonenumber = models.CharField(max_length=20)
    image1 = models.ImageField(default="defaultuser.jpg", upload_to="award/contestant/%Y/%m/%d")
    image2 = models.ImageField(default="defaultuser.jpg", upload_to="award/contestant/%Y/%m/%d")
    gender = models.CharField(max_length=10)
    number_of_votes = models.IntegerField(default=0)
    is_evicted = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"{self.firstname}|{self.id}"

    # def save(self,*args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.image1.path)
    #     if img.height > 120 or img.width > 120:
    #         img = img.resize((800,800), Image.ANTIALIAS)
    #         img.save(self.image1.path)

    #     img2 = Image.open(self.image2.path)
    #     if img2.height > 120 or img2.width > 120:
    #         img2 = img2.resize((800,800), Image.ANTIALIAS)
    #         img2.save(self.image2.path)

    @property
    def fullname(self):
        return f"{self.lastname} {self.firstname}"


class AwardVotePurchase(models.Model):
    ref = models.CharField(max_length=200)
    email = models.EmailField()
    number_of_votes = models.IntegerField(default=0)
    contestant_id = models.ForeignKey(AwardsContestant, on_delete=models.SET_NULL,null=True)
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
            object_with_similar_ref = AwardVotePurchase.objects.filter(ref = ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)