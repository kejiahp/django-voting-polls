import secrets
from django.db import models


class NewPageantRegistration(models.Model):
    height_measurement = [
        ("Ft", "Ft"),
        ("Mm", "Mm")
    ]
    experience_types = [
        ("beginner", "beginner"),
        ("intermediate", "intermediate"),
        ("professional", "professional")
    ]
    gender_types = [
        ("male", "male"),
        ("female", "female")
    ]

    firstname = models.CharField(max_length=300, blank=False)
    lastname = models.CharField(max_length=300, blank=False)
    instagram_handle = models.CharField(max_length=300, blank=False)
    email = models.EmailField(blank=False)
    date_of_birth = models.DateField(blank=False)
    height_type = models.CharField(choices=height_measurement, max_length=4)
    height = models.CharField(blank=False, max_length=10)
    gender = models.CharField(choices=gender_types, max_length=10)
    state_of_residence = models.CharField(max_length=300)
    is_in_agency = models.CharField(max_length=300, blank=False)
    phonenumber = models.CharField(max_length=20, blank=True, null=True)
    agency_name = models.CharField(max_length=300, blank=True)
    agency_image = models.ImageField(blank=True, null=True, default=None)
    modeling_experience = models.CharField(
        choices=experience_types, max_length=30, blank=True)
    image1 = models.ImageField(blank=False, null=False)
    image2 = models.ImageField(blank=True, null=True, default=None)
    image3 = models.ImageField(blank=True, null=True, default=None)

    number_of_votes = models.IntegerField(default=0)
    is_evicted = models.BooleanField(default=False)
    is_confirmed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-number_of_votes",)
        verbose_name = "Pageantry Registration"
        verbose_name_plural = "Pageantry Registrations"

    @property
    def fullname(self):
        if self.lastname == None:
            return f"{self.firstname}"
        if self.firstname == None:
            return f"{self.lastname}"
        else:
            return f"{self.lastname} {self.firstname}"

    def __str__(self) -> str:
        return f"Pageantry Contestant: {self.fullname} | {self.id}"
