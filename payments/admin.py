from django.contrib import admin
from .models import WebhookTestModel, NewVotingWebhookModel


class NewVotingWebhookModelAdmin(admin.ModelAdmin):
    search_fields = ['email', 'ref']
    list_filter = ['verified', 'type_of_vote', 'payment_state']


# Register your models here.
admin.site.register(WebhookTestModel)
admin.site.register(NewVotingWebhookModel, NewVotingWebhookModelAdmin)
