import secrets
from django.db import models
from django.utils import timezone


class AwardsCategory(models.Model):
    name = models.CharField(max_length=150)
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Awards categories"

    def __str__(self):
        return f"{self.name}"


class NewAwardsRegistration(models.Model):
    gender_types = [
        ("male", "male"),
        ("female", "female")
    ]

    categories = [
        ("VIDEO DIRECTOR OF THE YEAR", "VIDEO DIRECTOR OF THE YEAR"),
        ("PAGEANT ICON OF THE YEAR", "PAGEANT ICON OF THE YEAR"),
        ("ARTISTE OF THE YEAR", "ARTISTE OF THE YEAR"),
        ("MEDIA PERSONALITY OF THE YEAR", "MEDIA PERSONALITY OF THE YEAR"),
        ("ENTREPRENEUR OF THE YEAR", "ENTREPRENEUR OF THE YEAR"),
        ("CINEMATIC STAR OF THE YEAR", "CINEMATIC STAR OF THE YEAR"),
        ("SONG / ARTISTE OF THE YEAR", "SONG / ARTISTE OF THE YEAR"),
        ("BRAND OF THE YEAR", "BRAND OF THE YEAR"),
        ("DANCER OF THE YEAR", "DANCER OF THE YEAR"),
        ("MODEL OF THE YEAR OF THE YEAR", "MODEL OF THE YEAR OF THE YEAR"),
        ("COMEDIAN / SKITMAKER OF THE YEAR", "COMEDIAN / SKITMAKER OF THE YEAR"),
        ("FASHION DESIGNER OF THE YEAR", "FASHION DESIGNER OF THE YEAR"),
        ("REAL ESTATE COMPANY OF THE YEAR", "REAL ESTATE COMPANY OF THE YEAR"),
        ("SKINCARE BRAND OF THE YEAR", "SKINCARE BRAND OF THE YEAR"),
        ("CREATIVE DIRECTOR OF THE YEAR", "CREATIVE DIRECTOR OF THE YEAR"),
        ("MC OF THE YEAR", "MC OF THE YEAR"),
        ("ATHLETE OF THE YEAR", "ATHLETE OF THE YEAR"),
        ("SOCIAL MEDIA INFLUENCER OF THE YEAR",
         "SOCIAL MEDIA INFLUENCER OF THE YEAR"),
        ("CONTENT CREATOR OF THE YEAR", "CONTENT CREATOR OF THE YEAR"),
        ("TV STAR OF THE YEAR", "TV STAR OF THE YEAR"),
        ("MAKEUP ARTISTE OF THE YEAR", "MAKEUP ARTISTE OF THE YEAR"),
        ("CEO OF THE YEAR", "CEO OF THE YEAR"),
        ("CREATIVE OF THE YEAR", "CREATIVE OF THE YEAR"),
        ("WRITER / BLOGGER OF THE YEAR", "WRITER / BLOGGER OF THE YEAR"),
        ("DJ OF THE YEAR", "DJ OF THE YEAR"),
    ]

    firstname = models.CharField(max_length=300, blank=False)
    lastname = models.CharField(max_length=300, blank=False)
    email = models.EmailField(blank=False)

    category = models.ForeignKey(to=AwardsCategory, on_delete=models.CASCADE)

    date_birth = models.DateField(blank=False)
    instagram_handle = models.CharField(max_length=300, blank=False)
    gender = models.CharField(choices=gender_types,
                              max_length=300, blank=False)
    brand_name = models.CharField(max_length=300, blank=False)
    industry_years = models.IntegerField(blank=False)
    image = models.ImageField(blank=True, null=True, default=None)

    number_of_votes = models.IntegerField(default=0)
    is_evicted = models.BooleanField(default=False)
    is_confirmed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def fullname(self):
        if self.lastname == None:
            return f"{self.firstname}"
        if self.firstname == None:
            return f"{self.lastname}"
        else:
            return f"{self.lastname} {self.firstname}"

    class Meta:
        verbose_name = "Awards Registration"
        verbose_name_plural = "Awards Registrations"
        ordering = ("-number_of_votes",)

    def __str__(self) -> str:
        return f"Awards Contestant: {self.fullname} | {self.id}"
