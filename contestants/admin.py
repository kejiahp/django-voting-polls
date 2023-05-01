from django.contrib import admin
from contestants.models import NewPageantRegistration


class RegConstAdmin(admin.ModelAdmin):
    # Let you to search with title name, release year and length of duration of movie
    search_fields = ['firstname', 'lastname', 'email', 'phonenumber']
    # There will be a filter on release year
    list_filter = ['date_created', 'is_confirmed']


class RegPurchAdmin(admin.ModelAdmin):
    # Let you to search with first name, last name and phone number of the customer
    search_fields = ['phonenumber', 'email']
    # There will be a filter on last name
    list_filter = ['completed']


class NewPageantRegistrationsAdmin(admin.ModelAdmin):
    search_fields = ["firstname", "email", "lastname"]


# Register your models here.
admin.site.register(NewPageantRegistration, NewPageantRegistrationsAdmin)
