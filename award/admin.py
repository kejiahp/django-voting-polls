from django.contrib import admin
from award.models import AwardsCategory, NewAwardsRegistration


class AwardsCategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


class NewAwardsRegistrationAdmin(admin.ModelAdmin):
    search_fields = ['firstname', 'lastname', 'email', 'phonenumber']
    list_filter = ['category', 'created_at']


admin.site.register(NewAwardsRegistration, NewAwardsRegistrationAdmin)
admin.site.register(AwardsCategory, AwardsCategoryAdmin)
