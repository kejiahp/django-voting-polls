from django.contrib import admin
from award.models import AwardsCategory,AwardsContestant,AwardVotePurchase

class AwardsCategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']

class AwardsContestantAdmin(admin.ModelAdmin):
    search_fields = ['firstname', 'lastname', 'email', 'phonenumber']
    list_filter = ['category', 'date_created']

class AwardVotePurchaseAdmin(admin.ModelAdmin):
    search_fields = ['email', 'contestant_id', 'number_of_votes', 'amount']
    list_filter = ['verified']



admin.site.register(AwardsContestant, AwardsContestantAdmin)
admin.site.register(AwardsCategory, AwardsCategoryAdmin)
admin.site.register(AwardVotePurchase, AwardVotePurchaseAdmin)