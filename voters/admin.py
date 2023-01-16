from django.contrib import admin
from voters.models import VotePurchase,NewsLetterSubscriber

class VotePurchaseAdmin(admin.ModelAdmin):
    search_fields = ['email', 'contestant_id', 'number_of_votes', 'amount']
    list_filter = ['verified','date_created']

class NewsLetterSubscriberAdmin(admin.ModelAdmin):
    search_fields = ['email']

admin.site.register(VotePurchase, VotePurchaseAdmin)
admin.site.register(NewsLetterSubscriber, NewsLetterSubscriberAdmin)
