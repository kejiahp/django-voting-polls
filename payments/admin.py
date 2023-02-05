from django.contrib import admin
from .models import WebhookTestModel, AwardVotingWebhookModel

# Register your models here.
admin.site.register(WebhookTestModel)
admin.site.register(AwardVotingWebhookModel)
